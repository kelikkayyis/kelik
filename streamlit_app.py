import streamlit as st 
import plotly.express as px 
import matplotlib.pyplot as plt
import pandas as pd
import requests
from st_aggrid import AgGrid

# house = pd.read_csv('https://raw.githubusercontent.com/kelikkayyis/kelik/main/house_clean.csv')
titanic = pd.read_csv('https://raw.githubusercontent.com/mofdac/-materi-das/main/01.%20Python%20for%20DA/titanic.csv')

def main() : 
  # st.header('This is Header')
  # st.subheader('This is SubHeader')
  # st.markdown('# Rendering Markdown ')
  # st.write('Some Phytagorean Equation : ')
  # st.latex('c^2 = a^2+b^2')

  #matplotlib chart 
  st.subheader('Matplotlib')
  fig,ax = plt.subplots()
  plt.scatter(titanic['Age'],titanic['Fare'])
  st.pyplot(fig)

  st.subheader('Plotly')
  plotly_fig = px.scatter(titanic['Age'],titanic['Fare'])
  st.plotly_chart(plotly_fig)
  
if __name__ == '__main__' : 
  main()