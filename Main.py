import streamlit as st
import pandas as pd

st.title('Leetcode Contest Dashboard Generator')

file = st.file_uploader('Upload your Contest file here...')

if file:
  #Department wise Distribution
  data = pd.read_csv(file)

  years = ['All'] + list(data['Year'].value_counts().index)

  year_select = st.selectbox('Year', years, index=0)

  if year_select:
    filtered_data = pd.DataFrame()

    if year_select == 'All':
      filtered_data = data
    else:
      filtered_data = data[data.Year == year_select]

  col1, gap1, col2, gap2, col3 = st.columns([1, 0.3, 1, 0.2, 1])

  with col1:
    dept_counts = filtered_data['Department'].value_counts()
    dept = list(dept_counts.index)

    dept_df = pd.DataFrame({
      'Department' : dept,
      'Count' : dept_counts
    })

    st.bar_chart(dept_df, x='Department', y='Count')

  with col2:
    #Attended or not
    ranks = filtered_data['Rank']
    zero = 0

    for rank in ranks:
      if rank == 0:
        zero += 1

    nonzero = len(ranks) - zero

    presence_df = pd.DataFrame({
      'Presence' : ['Present', 'Absent'],
      'Count' : [nonzero, zero]
    })

    st.bar_chart(presence_df, x='Presence', y='Count')

  with col3:
    #Problem count
    problems_count = filtered_data['ProbCount'].value_counts()
    problems = list(problems_count.index)

    problem_df = pd.DataFrame({
      'Problems' : problems,
      'Count' : problems_count
    })

    st.bar_chart(problem_df, x='Problems', y='Count')
