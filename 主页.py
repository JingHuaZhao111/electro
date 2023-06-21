import streamlit as st
import pandas as pd
from util.statistics_and_rank import show_statistics
from util.produce_power_statistics import yes,today
from datetime import datetime
from util.time_restart import next_update_time
from streamlit_elements import elements, mui, html
from streamlit_elements import dashboard

st.set_page_config(
        layout="wide",
    )

# 标题
st.markdown("# Main Page")

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




# # 创建一个容器
# container = st.container()

# # 自定义容器的边框样式
# container_style = '''
#     <style>
#     .st-cn {
#         border: 1px solid red;
#         border-radius: 10px;
#         padding: 20px;
#     }
#     </style>
# '''

# # 在容器中添加其他组件
# with container:
#     st.title("这是一个容器示例")
#     st.write("这是容器中的内容。")
#     st.button("点击我")

# # 在容器外部添加其他组件
# st.header("容器外部的内容")
# st.write("这是容器外部的内容。")

# # 渲染自定义样式
# st.markdown(container_style, unsafe_allow_html=True)

