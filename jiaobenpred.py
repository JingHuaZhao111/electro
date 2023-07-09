import csv
import random
import time
import os
from datetime import datetime, timedelta
csv_paths = ["pred/1.csv", "pred/2.csv", "pred/3.csv", "pred/4.csv", "pred/5.csv", "pred/6.csv", "pred/7.csv", "pred/8.csv", "pred/9.csv", "pred/10.csv"]
header = ["TurbID", "DATATIME", "ROUND(A.POWER,0)", "YD15"]
# 定义时间间隔（以秒为单位）
interval = 10


for csv_path in csv_paths:
    file_name = os.path.basename(csv_path)  # 获取文件名（包括扩展名）
    file_name_without_extension = os.path.splitext(file_name)[0]  # 去除扩展名
    turb_id = file_name_without_extension.split("/")[-1]  # 提取数字部分
    # 获取昨天0点的时间
    yesterday = datetime.now()-timedelta(days=30)
    start_time = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
    
    # 生成15分钟递增的时间戳
    time_increment = timedelta(minutes=15)
    round_power = random.randint(0, 20000)
    yd15 = round(random.uniform(0, 20000), 1)

    # 将随机数据写入CSV文件
    with open(csv_path, mode="a", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        # 生成多个数据点
        for _ in range(4996):
            datatime = start_time.strftime("%Y/%m/%d %H:%M")
            round_power = random.randint(0, 20000)
            yd15 = round(random.uniform(0, 20000), 1)
            csv_writer.writerow([turb_id, datatime, round_power, yd15])
            
            start_time += time_increment
    # # 等待一定时间
    # time.sleep(interval)
