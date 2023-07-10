import streamlit as st
import pandas as pd
import os
import plotly.express as px
import time
from streamlit_extras.app_logo import add_logo
from streamlit_extras.colored_header import colored_header
st.set_page_config(
        layout="wide",
        page_icon="⚡",
    )
add_logo("picture\wind-turbine-2244222_640.jpg", height=175)
with st.sidebar:
        st.title("👷🏿‍♂️煤球发电")  
        from markdownlit import mdlit
        mdlit(
        "@(🏆)(百度飞浆)(https://aistudio.baidu.com/aistudio/index)"
        )  
        mdlit(
            "@(🏆)(软件杯)(https://www.cnsoftbei.com/)"
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
col1,col2=st.columns([3,1])
with col2:
    from streamlit_extras.switch_page_button import switch_page
    main_page = st.button("返回主页")
    if main_page:
        switch_page("主页")
    with st.expander("",expanded=True):
        selected_file = st.selectbox('选择风机', file_options)
        values = st.slider('显示范围', 0.0, 1.0, (0.97, 1.0))


if selected_file:
    file_name = selected_file.split('号')[0] + '.csv'
    file_name=os.path.join('data',file_name)
    df = pd.read_csv(file_name)  # 读取选定的Excel文件为DataFrame
    
    with col2:
        selected=st.multiselect(
        "选择特征",
        [c for c in df.columns if c!="DATATIME"],
        default=['YD15']
        )
    with col1: 
        start = int(len(df) * (values[0] ))
        end = int(len(df) * (values[1] ))
        data = df.iloc[start:end, :]
        from streamlit_extras.chart_container import chart_container
        with chart_container(data,tabs=("折线图 📈", "csv文件 📄", "导出 📁")):
            st.line_chart(data,x="DATATIME",y=selected)
    colored_header(
    label="",
    description="",
    color_name="yellow-80",)    
    # with st.container():
    #     # 创建一个空的占位符
    #     chart_placeholder = st.empty()
    #     # 设置绘图速度（延迟时间）
    #     delay = 0.01
    #     # 遍历每个数据点，并逐步绘制图表
    #     for i in range(len(data)):
    #         # 更新占位符内容，绘制图表
    #         data_to_plot = data.iloc[:i+1]
    #         chart_placeholder.line_chart(data_to_plot,x="DATATIME",y=selected)
    #         time.sleep(delay)

from streamlit_extras.dataframe_explorer import dataframe_explorer
con1=st.container()
with con1:
    filtered_df = dataframe_explorer(data, case=False)
    st.dataframe(filtered_df, use_container_width=True)