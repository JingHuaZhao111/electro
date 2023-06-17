import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta
from util.predict_chart import predict_df
import time

col1, col2 = st.columns(2)
with col2:
    with st.expander("参数调整", expanded=True):
        # Initialize session state
        if 'current_date' not in st.session_state:
            st.session_state.current_date = datetime.now().date()
        if 'max_date' not in st.session_state:
            st.session_state.max_date = st.session_state.current_date + timedelta(days=30)

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
        selected_fan = st.radio("选择风机号", ["1号风机", "2号风机", "3号风机", "4号风机", "5号风机", "6号风机", "7号风机", "8号风机", "9号风机", "10号风机"])
    # 创建按钮
    button_clicked = st.button("预测")

# 点击按钮后才会输出预测日期范围
if button_clicked:
    with col1:
        st.write("预测日期范围:", start_date, "到", end_date)
        df=predict_df(start_date,end_date,selected_features,selected_fan)
        if(len(selected_features)==2):
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
    
        if(len(selected_features)==3):
            # 创建一个空的占位符
            chart_placeholder = st.empty()
            # 设置绘图速度（延迟时间）
            delay = 0.02
            # 遍历每个数据点，并逐步绘制图表
            for i in range(len(df)):
                data_to_plot = df.iloc[:i+1].set_index('DATATIME')['ROUND(A.POWER,0)']
                # 更新占位符内容，绘制图表
                chart_placeholder.line_chart(data_to_plot)
                # 添加延迟，控制绘图速度
                time.sleep(delay)
            chart_placeholder = st.empty()
            # 设置绘图速度（延迟时间）
            delay = 0.05
            # 遍历每个数据点，并逐步绘制图表
            for i in range(len(df)):
                data_to_plot = df.iloc[:i+1].set_index('DATATIME')['YD15']
                # 更新占位符内容，绘制图表
                chart_placeholder.line_chart(data_to_plot)
                # 添加延迟，控制绘图速度
                time.sleep(delay)