import streamlit as st
import pandas as pd
from util.statistics_and_rank import show_statistics

st.title("Main Page")


st.dataframe(show_statistics())