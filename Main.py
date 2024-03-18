import streamlit as st
import pandas as pd

st.title('Leetcode Contest Dashboard Generator')

file = st.file_uploader('Upload your Contest file here...')

if file:
  data = pd.read_csv(file)

  col1, col2 = st.columns(2)

  with col1:
    dept_counts = list(data['Department'].value_counts())
    dept = list(dept_counts.index)

    dept_df = pd.DataFrame({
      'Department' : dept,
      'Count' : dept_counts
    })

    st.bar_chart(dept_df, x='Department', y='Count')
