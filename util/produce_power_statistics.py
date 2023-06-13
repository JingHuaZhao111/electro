import streamlit as st
import pandas as pd
import os
folder_path = 'data'
@st.cache_data
def yes_power(df):
    # 将DATATIME列解析为日期时间类型
    df['DATATIME'] = pd.to_datetime(df['DATATIME'])

    # 设置日期范围（这里以2021年11月1日为例）
    start_date = pd.to_datetime('2021-11-01')
    end_date = pd.to_datetime('2021-11-01') + pd.DateOffset(days=1)

    # 筛选出指定日期范围内的数据
    filtered_df = df[(df['DATATIME'] >= start_date) & (df['DATATIME'] < end_date)]
    # 计算YD15列的和
    yd15_sum = filtered_df['YD15'].sum()*0.25
    return yd15_sum
@st.cache_data
def today_power(df):
    # 将DATATIME列解析为日期时间类型
    df['DATATIME'] = pd.to_datetime(df['DATATIME'])

    # 设置日期范围（这里以2021年11月1日为例）
    start_date = pd.to_datetime('2021-11-01')
    end_date = pd.to_datetime('2021-11-01') + pd.DateOffset(days=1)

    # 筛选出指定日期范围内的数据
    filtered_df = df[(df['DATATIME'] >= start_date) & (df['DATATIME'] < end_date)]
    # 计算YD15列的和
    yd15_sum = filtered_df['YD15'].sum()*0.25
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