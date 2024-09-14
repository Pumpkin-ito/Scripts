from datetime import datetime

# 获取当前时间
current_time = datetime.now()

# 指定一个时间（例如 2024-09-12 12:00:00）
specified_time = datetime(2024, 9, 12, 18, 0, 0)

# 比较时间
if current_time > specified_time:
    print("当前时间在指定时间之后")
elif current_time < specified_time:
    print("当前时间在指定时间之前")
else:
    print("当前时间与指定时间相同")
