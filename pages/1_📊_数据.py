import streamlit as st
import pandas as pd
import os
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
selected_file = st.selectbox('选择风机', file_options)

if selected_file:
    file_name = selected_file.split('号')[0] + '.csv'
    file_name=os.path.join('data',file_name)
    df = pd.read_csv(file_name)  # 读取选定的Excel文件为DataFrame
    st.write(df)