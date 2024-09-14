from datetime import datetime
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

import GrabFunc as fc

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# 实例化Chrome浏览器驱动
driver = webdriver.Chrome()

# 使用Chrome浏览器驱动访问12306官方网站
driver.get("https://kyfw.12306.cn/otn/resources/login.html")

# 记录查询次数
query_times = 1

# 手动登录
fc.login(driver)

# 温馨提示
print("=========================抢票中=============================")

# 获取购票总信息
info = fc.read_info()
print(info["grab_time"])

# 获取乘客信息存为列表
passengers = info['passengers'].split()

# 进入查询页面，填写信息
fc.into_query(driver,info ,info['travel_date'])

# 判断时间
while True:
    if fc.compare_time(info["grab_time"]):
        print(datetime.now())
        break;

# 查询车票
fc.query_tickets(driver)

# 选择车次
trains = info["train_number"].split()

# 座位等级
seat_level = info["seat_level"].split()

# 座位位置
seat_position = info["seat_position"].split()

# 抢票循环
while True:
    print("查询次数:{0}".format(query_times))
    # 判断能否购买，可以购买进入选择乘客页
    fc.if_can_buy(driver, fc.list_to_string(trains),str(len(passengers)),fc.list_to_string(seat_level))
    mod = 0
    # 判断是否已经在购票页面
    if driver.current_url == 'https://kyfw.12306.cn/otn/confirmPassenger/initDc':
        while True:
            # 确认购买车票
            fc.confirm_buy(driver, fc.list_to_string(passengers) ,fc.list_to_string(seat_position),str(len(passengers)),mod)
            # 判断车票是否购买成功
            mod = fc.if_get_ticket(driver)
            if mod == 2 | mod == 3:
                break
    if mod == 2:
        break
    if (driver.current_url == 'https://www.12306.cn/mormhweb/logFiles/error.html') | (mod == 3):
        # 刷新页面
        fc.into_query(driver, info, info["travel_date"])
    # 重新查询
    fc.query_tickets(driver)
    # 增加查询次数
    query_times += 1
input("按任意键结束程序")

# 预填单网址
# https://kyfw.12306.cn/otn/view/prefill_list.html?from=IUQ&to=KMM&date=2024-09-26&fromName=%E5%8C%97%E4%BA%AC%E5%8D%97&toName=%E5%90%88%E8%82%A5