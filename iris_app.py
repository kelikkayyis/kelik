# Import library yang diperlukan
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load dataset Iris
iris = load_iris()
iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_data['species'] = [iris.target_names[i] for i in iris.target]

# Membuat halaman untuk tiap jenis Iris
st.title("Visualisasi Data Iris")

# Pilihan halaman
page = st.sidebar.selectbox("Pilih jenis Iris:", ["Setosa", "Versicolor", "Virginica"])

# Grafik untuk Setosa
if page == "Setosa":
    st.header("Setosa")
    setosa_data = iris_data[iris_data['species'] == 'setosa']
    
    st.subheader("Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(setosa_data['sepal length (cm)'], setosa_data['sepal width (cm)'], c='blue', label='Setosa')
    ax.set_xlabel('Sepal Length (cm)')
    ax.set_ylabel('Sepal Width (cm)')
    ax.legend()
    st.pyplot(fig)
    
    st.subheader("Histogram")
    fig, ax = plt.subplots()
    ax.hist(setosa_data['petal length (cm)'], bins=10, color='blue', label='Setosa')
    ax.set_xlabel('Petal Length (cm)')
    ax.set_ylabel('Frequency')
    ax.legend()
    st.pyplot(fig)

# Grafik untuk Versicolor
elif page == "Versicolor":
    st.header("Versicolor")
    versicolor_data = iris_data[iris_data['species'] == 'versicolor']
    
    st.subheader("Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(versicolor_data['sepal length (cm)'], versicolor_data['sepal width (cm)'], c='green', label='Versicolor')
    ax.set_xlabel('Sepal Length (cm)')
    ax.set_ylabel('Sepal Width (cm)')
    ax.legend()
    st.pyplot(fig)
    
    st.subheader("Histogram")
    fig, ax = plt.subplots()
    ax.hist(versicolor_data['petal length (cm)'], bins=10, color='green', label='Versicolor')
    ax.set_xlabel('Petal Length (cm)')
    ax.set_ylabel('Frequency')
    ax.legend()
    st.pyplot(fig)

# Grafik untuk Virginica
elif page == "Virginica":
    st.header("Virginica")
    virginica_data = iris_data[iris_data['species'] == 'virginica']
    
    st.subheader("Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(virginica_data['sepal length (cm)'], virginica_data['sepal width (cm)'], c='red', label='Virginica')
    ax.set_xlabel('Sepal Length (cm)')
    ax.set_ylabel('Sepal Width (cm)')
    ax.legend()
    st.pyplot(fig)
    
    st.subheader("Histogram")
    fig, ax = plt.subplots()
    ax.hist(virginica_data['petal length (cm)'], bins=10, color='red', label='Virginica')
    ax.set_xlabel('Petal Length (cm)')
    ax.set_ylabel('Frequency')
    ax.legend()
    st.pyplot(fig)
