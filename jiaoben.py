import csv
import random
import time
import os
from datetime import datetime, timedelta
csv_paths = ["data/1.csv", "data/2.csv", "data/3.csv", "data/4.csv", "data/5.csv", "data/6.csv", "data/7.csv", "data/8.csv", "data/9.csv", "data/10.csv"]
header = ["TurbID", "DATATIME", "WINDSPEED", "PREPOWER", "WINDDIRECTION", "TEMPERATURE", "HUMIDITY", "PRESSURE", "ROUND(A.WS,1)", "ROUND(A.POWER,0)", "YD15"]

# 定义时间间隔（以秒为单位）
interval = 10


for csv_path in csv_paths:
    file_name = os.path.basename(csv_path)  # 获取文件名（包括扩展名）
    file_name_without_extension = os.path.splitext(file_name)[0]  # 去除扩展名
    turb_id = file_name_without_extension.split("/")[-1]  # 提取数字部分
    # 获取昨天0点的时间
    yesterday = datetime.now()
    start_time = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
    
    # 生成15分钟递增的时间戳
    time_increment = timedelta(minutes=15)
    windspeed = round(random.uniform(0, 20), 1)
    prepower = random.randint(0, 20000)
    winddirection = random.randint(0, 360)
    temperature = round(random.uniform(-20, 50), 1)
    humidity = random.randint(0, 100)
    pressure = random.randint(800, 1200)
    round_ws = round(random.uniform(0, 20), 1)
    round_power = random.randint(0, 20000)
    yd15 = round(random.uniform(0, 20), 1)

    # 将随机数据写入CSV文件
    with open(csv_path, mode="a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        # 生成多个数据点
        for _ in range(480):
            datatime = start_time.strftime("%Y/%m/%d %H:%M")
            windspeed = round(random.uniform(0, 20), 1)
            prepower = random.randint(0, 20000)
            winddirection = random.randint(0, 360)
            temperature = round(random.uniform(-20, 50), 1)
            humidity = random.randint(0, 100)
            pressure = random.randint(800, 1200)
            round_ws = round(random.uniform(0, 20), 1)
            round_power = random.randint(0, 20000)
            yd15 = round(random.uniform(0, 20), 1)

            csv_writer.writerow([turb_id, datatime, windspeed, prepower, winddirection, temperature, humidity, pressure, round_ws, round_power, yd15])
            start_time += time_increment
    # # 等待一定时间
    # time.sleep(interval)
