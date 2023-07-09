import streamlit as st
import pandas as pd
from util.statistics_and_rank import show_statistics
from util.produce_power_statistics import yes,today
from datetime import datetime
from util.time_restart import next_update_time
from streamlit_elements import elements, mui, html
from streamlit_elements import dashboard
import time
from util.today_df import get_today_df,get_pre_today_df
st.set_page_config(
        page_title='煤球发电',
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
# 标题
# st.markdown("<span style='color:lawngreen; font-size:28px;'>Welcome</span>", unsafe_allow_html=True)


# 列
col1,col2=st.columns(spec = 2, gap = "large")

with col1:
    st.markdown('## 当前功率排名及预测')
    st.table(show_statistics())

with col2:
    # 获取当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    next_update = next_update_time()
    st.markdown(
        '<div style="text-align: right;">当前时间：{}</div>'.format(current_time),
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="text-align: right;">下一次更新的时间：{}</div>'.format(next_update.strftime("%Y-%m-%d %H:%M:%S")),
        unsafe_allow_html=True
    )
    selected_file = st.selectbox('选择风机', file_options)
    values1=get_today_df(selected_file[0])
    values2=get_pre_today_df(selected_file[0])
    values2=values2.rename(columns={'YD15':'PreYD15'})
    merge=pd.merge(values1,values2,on='DATATIME')
    st.line_chart(merge,x="DATATIME")
    
    
col3,col4=st.columns(spec = 2, gap = "large")
with col3:
    df = yes()
    st.markdown('## 昨日各风机发电量')
    st.bar_chart(df.set_index('ID')[['昨日发电量']])
with col4:
    df=today()
    st.markdown('## 今日截至目前各风机发电量')
    st.bar_chart(df.set_index('ID')[['今日目前发电量']])


