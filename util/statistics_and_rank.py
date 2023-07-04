import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from util.time_last import last_update_time
# 待修改为读取当日的信息
@st.cache_data()
def show_statistics():
    last_time=last_update_time()- timedelta(seconds=10)
    in_data_01=pd.read_csv('./data/1.csv')
    out_data_01=pd.read_csv('./pred/0001out.csv')
    in_row_01=in_data_01.iloc[2]
    out_row_01=out_data_01.iloc[2]

    in_data_02=pd.read_csv('./data/2.csv')
    out_data_02=pd.read_csv('./pred/0002out.csv')
    in_row_02=in_data_02.iloc[2]
    out_row_02=out_data_02.iloc[2]

    in_data_03=pd.read_csv('./data/3.csv')
    out_data_03=pd.read_csv('./pred/0003out.csv')
    in_row_03=in_data_03.iloc[2]
    out_row_03=out_data_03.iloc[2]

    in_data_04=pd.read_csv('./data/4.csv')
    out_data_04=pd.read_csv('./pred/0004out.csv')
    in_row_04=in_data_04.iloc[2]
    out_row_04=out_data_04.iloc[2]

    in_data_05=pd.read_csv('./data/5.csv')
    out_data_05=pd.read_csv('./pred/0005out.csv')
    in_row_05=in_data_05.iloc[2]
    out_row_05=out_data_05.iloc[2]

    in_data_06=pd.read_csv('./data/6.csv')
    out_data_06=pd.read_csv('./pred/0006out.csv')
    in_row_06=in_data_06.iloc[2]
    out_row_06=out_data_06.iloc[2]

    in_data_07=pd.read_csv('./data/7.csv')
    out_data_07=pd.read_csv('./pred/0007out.csv')
    in_row_07=in_data_07.iloc[2]
    out_row_07=out_data_07.iloc[2]

    in_data_08=pd.read_csv('./data/8.csv')
    out_data_08=pd.read_csv('./pred/0008out.csv')
    in_row_08=in_data_08.iloc[2]
    out_row_08=out_data_08.iloc[2]

    in_data_09=pd.read_csv('./data/9.csv')
    out_data_09=pd.read_csv('./pred/0009out.csv')
    in_row_09=in_data_09.iloc[2]
    out_row_09=out_data_09.iloc[2]

    in_data_10=pd.read_csv('./data/10.csv')
    out_data_10=pd.read_csv('./pred/0010out.csv')
    in_row_10=in_data_10.iloc[2]
    out_row_10=out_data_10.iloc[2]


    in_merge_10 = pd.concat([in_row_01, in_row_02,in_row_03,in_row_04,in_row_05,in_row_06,in_row_07,in_row_08,in_row_09,in_row_10], axis=1).T
    out_merge_10=pd.concat([out_row_01, out_row_02,out_row_03,out_row_04,out_row_05,out_row_06,out_row_07,out_row_08,out_row_09,out_row_10], axis=1).T
    out_merge_10=out_merge_10.drop(columns=['DATATIME','ROUND(A.POWER,0)'])
    in_merge_10=in_merge_10.drop(columns=['DATATIME','WINDSPEED','PREPOWER','WINDDIRECTION','TEMPERATURE','HUMIDITY','PRESSURE','ROUND(A.WS,1)','ROUND(A.POWER,0)'])
    out_merge_10=out_merge_10.rename(columns={'YD15':'Pred_YD15'})
    merged = pd.merge(in_merge_10, out_merge_10, on='TurbID', how='outer')
    merged=merged.sort_values(by='YD15', ascending=False).reset_index(drop=True)
    merged.index=merged.index+1
    merged.rename(columns={'TurbID': '风机号', 'YD15': '当前YD15','Pred_YD15':'下一时刻预测YD15'}, inplace=True)
    merged['风机号']=merged['风机号'].apply(lambda x: np.int64(round(x)))
    return merged

