import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta
from util.predict_chart import predict_df,real_df
import time
st.set_page_config(
        layout="wide",
    )
file_options = [
    '1号风机',
    '2号风机',
    '3号风机',
    '4号风机',
    '5号风机',
    '6号风机',
    '7号风机',
    '8号风机',
    '9号风机',
    '10号风机',
]
col1, col2 = st.columns([2,1])
with col2:
    with st.expander("参数调整", expanded=True):
        # Initialize session state
        if 'current_date' not in st.session_state:
            st.session_state.current_date = datetime.now().date()- timedelta(days=30)
        if 'max_date' not in st.session_state:
            st.session_state.max_date = datetime.now().date() + timedelta(days=1)

        # Get current date and calculate max date
        current_date = st.session_state.current_date
        max_date = st.session_state.max_date

        # Set start date input with limits
        start_date = st.date_input("选择预测开始日期",  max_value=max_date, value=current_date)

        # Set end date input with limits
        end_date = st.date_input("选择预测结束日期", min_value=start_date, max_value=max_date, value=max_date)

        # Update session state
        st.session_state.current_date = current_date
        st.session_state.max_date = max_date
        selected_features = st.multiselect("选择预测特征", ["YD15", "ROUND(A.POWER,0)"])
        # 添加单选框，用于选择风机号
        selected_file = st.selectbox('选择风机', file_options)
        # 创建按钮
    button_clicked1 = st.button("预测",type="primary")
    button_clicked2 = st.button("对比",type="primary")


# 点击按钮后才会输出预测日期范围
if button_clicked1:
    with col1:
        start_date=pd.to_datetime(start_date)
        end_date=pd.to_datetime(end_date)+ timedelta(days=1)-timedelta(minutes=15)
        st.write("预测日期范围:", start_date, "到", end_date)
        df = predict_df(start_date, end_date, selected_features, selected_file)
        if(len(selected_features)==1):
            # 创建一个空的占位符
            chart_placeholder = st.empty()
            # 设置绘图速度（延迟时间）
            delay = 0.02
            # 遍历每个数据点，并逐步绘制图表
            for i in range(len(df)):
                data_to_plot = df.iloc[:i+1].set_index('DATATIME')
                # 更新占位符内容，绘制图表
                chart_placeholder.line_chart(data_to_plot)
                # 添加延迟，控制绘图速度
                time.sleep(delay)

        if len(selected_features) == 2:
            # 创建两个空的占位符
            chart_placeholder1 = st.empty()
            chart_placeholder2 = st.empty()
            # 设置绘图速度（延迟时间）
            delay = 0.02
            # 遍历每个数据点，并逐步绘制图表
            for i in range(len(df)):
                data_to_plot_1 = df.iloc[:i + 1].set_index('DATATIME')['ROUND(A.POWER,0)']
                data_to_plot_2 = df.iloc[:i + 1].set_index('DATATIME')['YD15']
                # 更新占位符内容，绘制图表
                chart_placeholder1.line_chart(data_to_plot_1)
                chart_placeholder2.line_chart(data_to_plot_2)
                # 添加延迟，控制绘图速度
                time.sleep(delay)
if button_clicked2:
    with col1:
        start_date=pd.to_datetime(start_date)
        end_date=pd.to_datetime(end_date)+ timedelta(days=1)-timedelta(minutes=15)
        st.write("预测日期范围:", start_date, "到", end_date)
        df = predict_df(start_date, end_date, selected_features, selected_file)
        df_real = real_df(start_date, end_date, selected_features, selected_file)
        if(len(selected_features)==1):
            df=df.rename(columns={selected_features[0]:'Pre'+selected_features[0]})
            max_len=max(len(df),len(df_real))
            merge=pd.merge(df,df_real,on='DATATIME',how='outer')
            merge=merge.dropna(how='any')
            # 创建一个空的占位符
            chart_placeholder = st.empty()
            # 设置绘图速度（延迟时间）
            delay = 0.02
            # 遍历每个数据点，并逐步绘制图表
            for i in range(len(merge)):
                data_to_plot = merge.iloc[:i+1].set_index('DATATIME')
                chart_placeholder.line_chart(data_to_plot)
                # 添加延迟，控制绘图速度
                time.sleep(delay)

        if len(selected_features) == 2:
            df=df.rename(columns={'YD15':'PreYD15','ROUND(A.POWER,0)':'PreROUND(A.POWER,0)'})
            max_len=max(len(df),len(df_real))
            merge=pd.merge(df,df_real,on='DATATIME',how='outer')
            merge=merge.dropna(how='any')
            print(merge)
            # 创建两个空的占位符
            chart_placeholder1 = st.empty()
            chart_placeholder2 = st.empty()
            # 设置绘图速度（延迟时间）
            delay = 0.02
            # 遍历每个数据点，并逐步绘制图表
            for i in range(len(merge)):
                data_to_plot_1 = merge.iloc[:i + 1].set_index('DATATIME')[['ROUND(A.POWER,0)','PreROUND(A.POWER,0)']]
                data_to_plot_2 = merge.iloc[:i + 1].set_index('DATATIME')[['YD15','PreYD15']]
                # 更新占位符内容，绘制图表
                chart_placeholder1.line_chart(data_to_plot_1)
                chart_placeholder2.line_chart(data_to_plot_2)
                # 添加延迟，控制绘图速度
                time.sleep(delay)
