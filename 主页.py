import streamlit as st
import pandas as pd
from util.statistics_and_rank import show_statistics

st.title("Main Page")

col1,col2=st.columns([3,1])
with col1:
    st.dataframe(show_statistics())

