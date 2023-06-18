import streamlit as st
import pandas as pd
from util.statistics_and_rank import show_statistics
from util.produce_power_statistics import yes,today
from datetime import datetime
from util.time_restart import next_update_time
from streamlit_elements import elements, mui, html
from streamlit_elements import dashboard
import altair as alt
st.set_page_config(
        layout="wide",
    )


# 获取当前时间
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
next_update = next_update_time()
st.markdown(

    '当前时间：{}</div>'.format(current_time),
    unsafe_allow_html=True
)
st.markdown(
    '下一次更新的时间：{}</div>'.format(next_update.strftime("%Y-%m-%d %H:%M:%S")),
    unsafe_allow_html=True
)

# 列
col1,col2=st.columns(spec = 2, gap = "large")
with col1:
        st.markdown('## 当前功率排名及预测')
        st.table(show_statistics())

with col2:
    df = yes()
    st.markdown('## 昨日各风机发电量')
    st.bar_chart(df.set_index('ID')[['昨日发电量']])

df=today()
st.markdown('## 今日截至目前各风机发电量')
st.bar_chart(df.set_index('ID')[['今日目前发电量']])
