import streamlit as st
import pandas as pd
from util.statistics_and_rank import show_statistics
from util.produce_power_statistics import yes,today

st.markdown("# Main Page")

col1,col2=st.columns(2)
with col1:
    st.markdown('## 当前功率排名及预测')
    st.table(show_statistics())

with col2:
    df=yes()
    st.markdown('## 昨日各风机发电量')
    st.bar_chart(df.set_index('ID')[['昨日发电量']])
    
df=today()
st.markdown('## 今日截至目前各风机发电量')
st.bar_chart(df.set_index('ID')[['今日目前发电量']])