import streamlit as st
import pandas as pd
import os
import plotly.express as px
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
col1,col2=st.columns(2)
with col2:
    with st.expander("",expanded=True):
        selected_file = st.selectbox('选择风机', file_options)
        values = st.slider('显示范围', 0.0, 1.0, (0.97, 1.0))


if selected_file:
    file_name = selected_file.split('号')[0] + '.csv'
    file_name=os.path.join('data',file_name)
    df = pd.read_csv(file_name)  # 读取选定的Excel文件为DataFrame
    with col1:  
        start = int(len(df) * (values[0] ))
        end = int(len(df) * (values[1] ))
        data = df.iloc[start:end, :]
        st.write(data)
    with col2:
        selected=st.multiselect(
        "选择特征",
        [c for c in df.columns if c!="DATATIME"],
        default=['YD15']
        )
        
    with st.container():
        # 创建一个空的占位符
        chart_placeholder = st.empty()
        # 设置绘图速度（延迟时间）
        delay = 0.01
        # 遍历每个数据点，并逐步绘制图表
        for i in range(len(data)):
            # 更新占位符内容，绘制图表
            data_to_plot = data.iloc[:i+1]
            chart_placeholder.line_chart(data_to_plot,x="DATATIME",y=selected)
            time.sleep(delay)