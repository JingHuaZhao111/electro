import streamlit as st
import pandas as pd
import os
col1, col2 = st.columns(2)

with col2:
    with st.expander("参数调整", expanded=True):
        # 添加两个日期选择器，用于选择预测开始日期和结束日期
        start_date = st.date_input("选择预测开始日期")
        end_date = st.date_input("选择预测结束日期")
        selected_features = st.multiselect("选择预测特征", ["YD15", "Round"])
        # 添加单选框，用于选择风机号
        selected_fan = st.radio("选择风机号", ["1号风机", "2号风机", "3号风机", "4号风机", "5号风机", "6号风机", "7号风机", "8号风机", "9号风机", "10号风机"])
    # 创建按钮
    button_clicked = st.button("预测")

# 点击按钮后才会输出预测日期范围
if button_clicked:
    with col1:
        st.write("预测日期范围:", start_date, "到", end_date)

# 画图绘制预测结果