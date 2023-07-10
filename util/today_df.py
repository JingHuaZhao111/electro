import pandas as pd
import datetime
from datetime import timedelta
def get_today_df(ID):
    now = datetime.datetime.now()+timedelta(hours=8)
    # 指定CSV文件路径
    csv_file = 'data/'+ID+'.csv'
    # 获取当前日期
    current_date = datetime.date.today()
    # 读取CSV文件
    df = pd.read_csv(csv_file)
    # 将DATATIME列解析为日期类型
    df['DATATIME'] = pd.to_datetime(df['DATATIME'])
    # 筛选出今天到目前为止的行
    filtered_df = df[(df['DATATIME'].dt.date == current_date)&(df['DATATIME'] <=now)]
    # 获取YD15列的值
    yd15_values = filtered_df[['YD15', 'DATATIME']]
    return yd15_values
def get_pre_today_df(ID):
    now = datetime.datetime.now()+timedelta(hours=8)
    # 指定CSV文件路径
    csv_file = 'pred/'+ID+'.csv'
    # 获取当前日期
    current_date = datetime.date.today()
    # 读取CSV文件
    df = pd.read_csv(csv_file)
    # 将DATATIME列解析为日期类型
    df['DATATIME'] = pd.to_datetime(df['DATATIME'])
    # 筛选出今天到目前为止的行
    filtered_df = df[(df['DATATIME'].dt.date == current_date)&(df['DATATIME'] <=now)]
    # 获取YD15列的值
    yd15_values = filtered_df[['YD15', 'DATATIME']]
    return yd15_values