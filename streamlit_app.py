import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Set theme to change sidebar color
st.set_page_config(
    page_title="Iris Data Visualisation",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to change the color of the sidebar
st.markdown(
    """
    <style>
    .css-18e3th9 {
        background-color: #FFA500 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    # Load dataset Iris
    iris = load_iris()
    iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)
    iris_data['species'] = [iris.target_names[i] for i in iris.target]

    # Pilihan halaman dengan tabs
    st.sidebar.header("Navigasi")
    tab = st.sidebar.radio("Pilih halaman:", ["Setosa", "Versicolor", "Virginica", "Show Data"])

    # Grafik untuk Setosa
    if tab == "Setosa":
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
    elif tab == "Versicolor":
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
    elif tab == "Virginica":
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

    # Halaman untuk Show Data dengan filter
    elif tab == "Show Data":
        st.header("Show Data Iris")

        # Filter species
        species_tab = st.radio("Filter by Species:", options=["All", "Setosa", "Versicolor", "Virginica"])
        if species_tab == "Setosa":
            filtered_data = iris_data[iris_data['species'] == 'setosa']
        elif species_tab == "Versicolor":
            filtered_data = iris_data[iris_data['species'] == 'versicolor']
        elif species_tab == "Virginica":
            filtered_data = iris_data[iris_data['species'] == 'virginica']
        else:
            filtered_data = iris_data

        # Filter numeric columns
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            min_sepal_length, max_sepal_length = st.slider(
                "Sepal Length (cm)", 
                float(filtered_data['sepal length (cm)'].min()), 
                float(filtered_data['sepal length (cm)'].max()), 
                (float(filtered_data['sepal length (cm)'].min()), float(filtered_data['sepal length (cm)'].max()))
            )
        
        with col2:
            min_sepal_width, max_sepal_width = st.slider(
                "Sepal Width (cm)", 
                float(filtered_data['sepal width (cm)'].min()), 
                float(filtered_data['sepal width (cm)'].max()), 
                (float(filtered_data['sepal width (cm)'].min()), float(filtered_data['sepal width (cm)'].max()))
            )
        
        with col3:
            min_petal_length, max_petal_length = st.slider(
                "Petal Length (cm)", 
                float(filtered_data['petal length (cm)'].min()), 
                float(filtered_data['petal length (cm)'].max()), 
                (float(filtered_data['petal length (cm)'].min()), float(filtered_data['petal length (cm)'].max()))
            )
        
        with col4:
            min_petal_width, max_petal_width = st.slider(
                "Petal Width (cm)", 
                float(filtered_data['petal width (cm)'].min()), 
                float(filtered_data['petal width (cm)'].max()), 
                (float(filtered_data['petal width (cm)'].min()), float(filtered_data['petal width (cm)'].max()))
            )

        # Apply filters
        filtered_data = filtered_data[
            (filtered_data['sepal length (cm)'] >= min_sepal_length) & (filtered_data['sepal length (cm)'] <= max_sepal_length) &
            (filtered_data['sepal width (cm)'] >= min_sepal_width) & (filtered_data['sepal width (cm)'] <= max_sepal_width) &
            (filtered_data['petal length (cm)'] >= min_petal_length) & (filtered_data['petal length (cm)'] <= max_petal_length) &
            (filtered_data['petal width (cm)'] >= min_petal_width) & (filtered_data['petal width (cm)'] <= max_petal_width)
        ]

        st.write(filtered_data)

if __name__ == '__main__':
    main()
