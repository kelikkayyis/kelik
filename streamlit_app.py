import streamlit as st 
import pandas as pd 
import requests
from st_aggrid import AgGrid

#baca dataframe dari file csv 
house = pd.read_csv('https://raw.githubusercontent.com/kelikkayyis/kelik/main/house_clean.csv')

#read json file dari data covid 
flight_passanger_api = requests.post('https://forecastpassengerapi.herokuapp.com/forecast_timeseries',json={
  "month_limit": "2020-01-01",
  "window_size": 12
}).json()

def main() : 
  
  st.write('Contoh dataframe')
  st.dataframe(house)

  st.write('Contoh JSON')
  st.json(flight_passanger_api)
  st.write('Metrics')
  st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
  
  st.write('Menampilkan Dataframe dengan St AgGrid')
  AgGrid(house)
  st.table([x for x in range(1,5)])
  
if __name__ == '__main__' : 
  main()