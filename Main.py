import streamlit as st
import pandas as pd

st.title('Leetcode Contest Dashboard Generator')

file = st.file_uploader('Upload your Contest file here...')

if file:
  #Department wise Distribution
  data = pd.read_csv(file)

  col1, col2 = st.columns(2)

  with col1:
    dept_counts = data['Department'].value_counts()
    dept = list(dept_counts.index)

    dept_df = pd.DataFrame({
      'Department' : dept,
      'Count of student' : list(dept_counts)
    })

    st.bar_chart(dept_df, x='Department', y='Count of students')

  # with col2:
  #   #Attended or not
  #   ranks = data['Rank']
  #   zero = 0

  #   for rank in ranks:
  #     if rank == 0:
  #       zero += 1

  #   nonzero = len(ranks) - zero

  #   presence_df = pd.DataFrame({
  #     'Presence' : ['Present', 'Absent'],
  #     'Count' : [nonzero, zero]
  #   })

  #   st.bar_chart(presence_df, x='Presence', y='Count')
