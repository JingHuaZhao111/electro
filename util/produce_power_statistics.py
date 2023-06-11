import streamlit as st
import pandas as pd
def cal_power(df):
    # 将DATATIME列解析为日期时间类型
    df['DATATIME'] = pd.to_datetime(df['DATATIME'])

    # 设置日期范围（这里以2021年11月1日为例）
    start_date = pd.to_datetime('2021-11-01')
    end_date = pd.to_datetime('2021-11-01') + pd.DateOffset(days=1)

    # 筛选出指定日期范围内的数据
    filtered_df = df[(df['DATATIME'] >= start_date) & (df['DATATIME'] < end_date)]
    # 计算YD15列的和
    yd15_sum = filtered_df['YD15'].sum()*0.25
# 计算昨日发电总量
def yesterday_power():
    df = pd.read_csv('data/1.csv')
