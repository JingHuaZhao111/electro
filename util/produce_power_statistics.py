import streamlit as st
import pandas as pd
import os
import datetime

folder_path = 'data'

@st.cache_data

def yes_power(df):
    # 获取昨天的日期
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday_start = datetime.datetime(yesterday.year, yesterday.month, yesterday.day)
    yesterday_end = yesterday_start + pd.DateOffset(days=1)
    # 将DATATIME列解析为日期时间类型
    df['DATATIME'] = pd.to_datetime(df['DATATIME'])
    # 筛选出昨天的数据
    filtered_df = df[(df['DATATIME'] >= yesterday_start) & (df['DATATIME'] < yesterday_end)]
    # 计算YD15列的和
    yd15_sum = filtered_df['YD15'].sum() * 0.25
    return yd15_sum

@st.cache_data
def today_power(df):
    # 获取当前日期和时间
    now = datetime.datetime.now()
    start_date = datetime.datetime(now.year, now.month, now.day)  # 今天的起始日期
    end_date = now  # 当前日期和时间

    # 将DATATIME列解析为日期时间类型
    df['DATATIME'] = pd.to_datetime(df['DATATIME'])

    # 筛选出指定日期范围内的数据
    filtered_df = df[(df['DATATIME'] >= start_date) & (df['DATATIME'] <= end_date)]

    # 计算YD15列的和
    yd15_sum = filtered_df['YD15'].sum() * 0.25

    return yd15_sum
@st.cache_data
# 计算发电总量
def yes():
    all_data = pd.DataFrame()
    file_list = os.listdir(folder_path)
    for file in file_list:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        # 汇总所有的cal_power(df)结果，索引是文件名
        yes_power_sum = yes_power(df)
        file_name = file.replace('.csv', '')
        result = pd.Series([file_name, yes_power_sum], name='Data')  # 设置Series的名称为"Data"
        all_data = all_data.append(result)

    all_data.rename(columns={0: 'ID', 1: '昨日发电量'}, inplace=True)
    all_data['ID'] = all_data['ID'].astype(int)
    all_data.sort_values('ID', inplace=True)
    return all_data

@st.cache_data
# 计算发电总量
def today():
    all_data = pd.DataFrame()
    file_list = os.listdir(folder_path)
    for file in file_list:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        # 汇总所有的cal_power(df)结果，索引是文件名
        today_power_sum = today_power(df)
        file_name = file.replace('.csv', '')
        result = pd.Series([file_name, today_power_sum], name='Data')  # 设置Series的名称为"Data"
        all_data = all_data.append(result)

    all_data.rename(columns={0: 'ID', 1: '今日目前发电量'}, inplace=True)
    all_data['ID'] = all_data['ID'].astype(int)
    all_data.sort_values('ID', inplace=True)
    return all_data