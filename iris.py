import pandas as pd
import numpy as np
import streamlit as st
import pickle

# Fungsi untuk prediksi
def predict(input_data):
    clf = joblib.load("iris_xgb.pkl")  # Pastikan path benar
    return clf.predict(input_data)

# Definisikan species untuk hasil prediksi
species = ['setosa', 'versicolor', 'virginica']

# Judul aplikasi
st.title("Iris Flower Classification")
st.write("This app classifies iris flower among 3 possible species.")

# Sidebar untuk input
st.sidebar.title("Inputs")
sepal_length = st.sidebar.number_input("Sepal length (cm)", 4.3, 7.9, 5.0)
sepal_width = st.sidebar.number_input("Sepal width (cm)", 2.0, 4.4, 3.6)
petal_length = st.sidebar.number_input("Petal length (cm)", 1.0, 6.9, 1.4)
petal_width = st.sidebar.number_input("Petal width (cm)", 0.1, 2.5, 0.2)

# Tombol prediksi
if st.button("Predict"):
    # Buat array input
    inp = np.array([sepal_length, sepal_width, petal_length, petal_width])
    inp = np.expand_dims(inp, axis=0)
    
    # Prediksi
    prediction = predict(inp)

    # Tampilkan hasil
    result = species[np.argmax(prediction)]
    st.write("**This flower belongs to the " + result + " class**")
