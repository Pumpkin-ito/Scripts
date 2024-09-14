import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime



# 从配置文件读取配置
def read_info():
    info_file = open("Ticket-Info.ini", encoding='UTF-8')
    info = {}
    lines = info_file.readlines()
    for line in lines:
        if re.match(r'[^;]+=.*', line) != None :
            line = line.strip('\n')
            line = line.split("=")
            info[line[0].strip()] = line[1].strip()
    return info

# 登录
def login(driver):
    # 执行js脚本选择账号密码登陆
    try:
        WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.CLASS_NAME,"login-hd")))
        driver.execute_script('var c = document.querySelectorAll(".login-hd-account > a:nth-child(1)");c[0].click();')
    except Exception as e:
        print(e)
    input("登陆成功后，按任意键继续")

# 进入查询页面并且填写个人信息
def into_query(driver,info, travel_date):
    # 进入车票查询网址
    driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

    try:
        # 设置出发地点
        s = driver.find_element(by=By.ID, value="fromStationText")
        ActionChains(driver).move_to_element(s)\
        .click(s)\
        .send_keys_to_element(s, info["s_station"]) \
        .perform()
        y = driver.find_element(by=By.ID, value='citem_2')
        ActionChains(driver).move_to_element(y)\
        .click(y)\
        .perform()

        # 设置目的地点
        e = driver.find_element(by=By.ID, value="toStationText")
        ActionChains(driver).move_to_element(e)\
        .click(e)\
        .send_keys_to_element(e, info["e_station"]) \
        .perform()
        y = driver.find_element(by=By.ID, value='citem_0')
        ActionChains(driver).move_to_element(y)\
        .click(y)\
        .perform()

        # 填写出发日期
        driver.execute_script(f'document.getElementById("train_date").value=\'{travel_date}\';')
    except Exception as e:
        print(e)


def query_tickets(driver):
    # 点击查询
    try:
        driver.execute_script('document.getElementById("query_ticket").click();')
    except Exception as e:
        print(e)

# 将数组转为字符串形式，以便在Js中能够使用
def list_to_string(li):
    t_n = ""
    for x in li:
        t_n += '"'+str(x)+'",'
    t_n = '['+t_n+']'
    return t_n


# 比较时间
def compare_time(time_str):
    # 将传入的字符串转换为 datetime 对象，格式为 "%Y-%m-%d %H:%M:%S"
    specified_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

    # 获取当前时间
    current_time = datetime.now()

    # 比较当前时间和指定时间
    if current_time >= specified_time:
        return 1
    elif current_time < specified_time:
        return 0


# 判断是否有票
def if_can_buy(driver,train_number,passengers_num,seat_level):
    # 检查是否在查票页面
    if driver.current_url != 'https://kyfw.12306.cn/otn/leftTicket/init':
        return
    js ='try{var tb = document.getElementById("queryLeftTable");\
        var rows = tb.children;\
        var train_number = '+train_number+';\
        var passengers_num = '+passengers_num+';\
        var seat_level = '+seat_level+';\
        var length = rows.length;\
        for (var i = 0; i <length; i++) {\
            if(rows[i].children.length==0)continue;\
            try{\
                var number = rows[i].children[0].children[0]\
                .children[0].children[0].textContent.trim(); \
            }\
            catch(err){\
                continue;\
            }\
            if(train_number.indexOf(number)==-1)\
                continue;\
            for (var j = seat_level.length - 1; j >= 0; j--){\
                try{\
                    if(rows[i].children[seat_level[j]].textContent == "有"){\
                        rows[i].lastElementChild.firstChild.click();\
                    }\
                    if(rows[i].children[seat_level[j]].textContent >=passenger_num){\
                        rows[i].lastElementChild.firstChild.click();\
                    }\
                }\
                catch(err){\
                    continue;\
                }\
            }\
        }}catch{}'
    driver.execute_script(js)


# 点击下单，确认购买
def confirm_buy(driver, passengers, seat_position,passengers_num,mod):
    if mod == 0 :
        try:
            ticket = WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.ID,"ticket_tit_id")))
        except Exception as e:
            print('订票处报错')

        print("为您预订：{0}".format(ticket.text))

        js_order ='var passengers='+passengers+';\
            console.log(passengers);\
            var passengers_list = document.getElementById("normal_passenger_id");\
            var li = passengers_list.children;\
            for(var i = 0; i<li.length; i++){\
                if(passengers.indexOf(li[i].children[1].textContent)==-1){\
                    continue;\
                }\
                if(li[i].children[1].classList.value=="colorA"){continue;}\
                li[i].children[0].click();\
            }\
            document.getElementById("submitOrder_id").click();'
        driver.execute_script(js_order)
    if mod == 0 | mod == 1:
        print('开始选座')
        # 选座
        try:
            WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.ID, "qr_submit_id")))
        except Exception as e:
            print('选座处报错')

        js_set_seat ='var seat_position ='+seat_position+';\
            var passengers_num ='+passengers_num+';\
            var num_rows = Math.ceil(passengers_num / 2);\
            var mod = document.getElementById("selectNo").textContent.split("/");\
            if(mod[0] !== mod[1]){\
                for (row = 1; row <= num_rows; row++) {\
                    for (i = 0; i < seat_position.length; i++) {\
                        if (passengers_num === 0) {\
                            break;\
                        }else{\
                            passengers_num--;\
                            document.getElementById(row + seat_position[i]).click();\
                        }\
                    }\
                }\
            }'
        driver.execute_script(js_set_seat)

        qr_submit = driver.find_element(By.ID, "qr_submit_id")
        count = 0
        while True:
            try:
                time.sleep(0.5)
                qr_submit_color = qr_submit.value_of_css_property('color')
                if '(255, 255, 255' in qr_submit_color:
                    qr_submit.click()
                    WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.ID, "orderResultInfo_id")))
                    break
                count += 1
                if count == 5:
                    break
            except Exception as e:
                print('确认下单处报错')
                break

# 判断抢票是否成功
def if_get_ticket(driver):
    try:
        ticket_tip_common = driver.find_element(By.XPATH, '//*[@id="orderResultInfo_id"]/div').text
        if '请稍候' in ticket_tip_common:
            mod = 4
            return mod
        else:
            if ('本次列车已无满足您需求的集中席位' in ticket_tip_common) | (
                    '本次列车已无满足您需求的集中席位' in ticket_tip_common):
                print("订单已提交，请登录12306完成支付")
                mod = 2
                return mod
            elif ('订单已经提交' in ticket_tip_common):
                print("订单已提交，请登录12306完成支付")
                mod = 2
                return mod
            elif ('出票失败' in ticket_tip_common) | ('订票失败' in ticket_tip_common) | (
                    '网络忙，请稍后再试。' in ticket_tip_common):
                mod = 3
                return mod
            else:
                mod = 1
                return mod
                print(ticket_tip_common)
    except Exception as e:
        print("判断抢票错误" + f"{e}")
        mod = 1
        return mod

# 测试用例
# var seat_position = ["D", "F",];
# var passengers_num = 5;
# var num_rows = Math.floor(passengers_num / 2);  // 提前保存行数
#
# for (row = 1; row <= num_rows; row++) {
#     for (i = 0; i < seat_position.length; i++) {
#         if (passengers_num === 0) {  // 比较时用 ===
#             break;  // 乘客用完，跳出循环
#         } else {
#             passengers_num--;  // 减少乘客数量
#             document.getElementById(row + seat_position[i]).click(); // 输出相应座位
#         }
#     }
# }


