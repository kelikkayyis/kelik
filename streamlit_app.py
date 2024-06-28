import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.datasets import load_iris
from prediction import predict

# Mengatur konfigurasi halaman
st.set_page_config(
    page_title="Iris Data Visualisation",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk mengubah warna sidebar
st.markdown(
    """
    <style>
    /* Mengubah warna sidebar */
    .css-1lcbmhc {
        background-color: #FFA500 !important; /* Oranye */
    }
    .css-18e3th9 {
        padding-top: 3rem !important;
    }
    .css-18ni7ap {
        padding: 1.5rem 1rem 0 !important;
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

    # Menampilkan judul halaman utama
    st.title("Visualisasi Data Iris")

    # Pilihan halaman dengan tabs
    tab = st.sidebar.radio("Pilih halaman:", ["Iris Data", "Setosa", "Versicolor", "Virginica", "Prediction"])

    # Halaman untuk Show Data dengan filter
    if tab == "Iris Data":
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
        
    # Grafik untuk Setosa
    elif tab == "Setosa":
        st.header("Setosa")
        setosa_data = iris_data[iris_data['species'] == 'setosa']
        
        st.subheader("Scatter Plot")
        fig = px.scatter(
            setosa_data, 
            x='sepal length (cm)', 
            y='sepal width (cm)', 
            color=px.Constant('Setosa'),
            labels={'color': 'Species'},
            title="Scatter Plot Sepal Setosa"
        )
        fig.update_traces(marker=dict(color='blue'))
        st.plotly_chart(fig)
        
        st.subheader("Histogram")
        x_option = st.selectbox(
            "Pilih kolom untuk X-Axis:",
            options=setosa_data.columns[:-1],  # Semua kolom kecuali 'species'
            index=0
        )
        
        fig = px.histogram(
            setosa_data, 
            x=x_option, 
            nbins=10, 
            title=f"Histogram of {x_option} for Setosa",
            labels={x_option: x_option, 'count': 'Frequency'}
        )
        fig.update_traces(marker_color='blue')
        st.plotly_chart(fig)

    # Grafik untuk Versicolor
    elif tab == "Versicolor":
        st.header("Versicolor")
        versicolor_data = iris_data[iris_data['species'] == 'versicolor']
        
        st.subheader("Scatter Plot")
        fig = px.scatter(
            versicolor_data, 
            x='sepal length (cm)', 
            y='sepal width (cm)', 
            color=px.Constant('Versicolor'),
            labels={'color': 'Species'},
            title="Scatter Plot Sepal Versicolor"
        )
        fig.update_traces(marker=dict(color='green'))
        st.plotly_chart(fig)
        
        st.subheader("Histogram")
        x_option = st.selectbox(
            "Pilih kolom untuk X-Axis:",
            options=versicolor_data.columns[:-1],  # Semua kolom kecuali 'species'
            index=0
        )
        
        fig = px.histogram(
            versicolor_data, 
            x=x_option, 
            nbins=10, 
            title=f"Histogram of {x_option} for Versicolor",
            labels={x_option: x_option, 'count': 'Frequency'}
        )
        fig.update_traces(marker_color='green')
        st.plotly_chart(fig)

    # Grafik untuk Virginica
    elif tab == "Virginica":
        st.header("Virginica")
        virginica_data = iris_data[iris_data['species'] == 'virginica']
        
        st.subheader("Scatter Plot")
        fig = px.scatter(
            virginica_data, 
            x='sepal length (cm)', 
            y='sepal width (cm)', 
            color=px.Constant('Virginica'),
            labels={'color': 'Species'},
            title="Scatter Plot Sepal Virginica"
        )
        fig.update_traces(marker=dict(color='red'))
        st.plotly_chart(fig)
        
        st.subheader("Histogram")
        x_option = st.selectbox(
            "Pilih kolom untuk X-Axis:",
            options=virginica_data.columns[:-1],  # Semua kolom kecuali 'species'
            index=0
        )
        
        fig = px.histogram(
            virginica_data, 
            x=x_option, 
            nbins=10, 
            title=f"Histogram of {x_option} for Virginica",
            labels={x_option: x_option, 'count': 'Frequency'}
        )
        fig.update_traces(marker_color='red')
        st.plotly_chart(fig)

    # Prediction Iris Species
    elif tab == "Prediction":
        species_mapping = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

        st.title('Classifying Iris Flowers')
        st.markdown('Toy model to play to classify iris flowers into \
             (setosa, versicolor, virginica) based on their sepal/petal \
            and length/width.')

        st.header("Plant Features")
        col1, col2 = st.columns(2)

        with col1:
            st.text("Sepal characteristics")
            sepal_l = st.slider('Sepal lenght (cm)', 1.0, 8.0, 0.5)
            sepal_w = st.slider('Sepal width (cm)', 2.0, 4.4, 0.5)

        with col2:
            st.text("Petal characteristics")
            petal_l = st.slider('Petal lenght (cm)', 1.0, 7.0, 0.5)
            petal_w = st.slider('Petal width (cm)', 0.1, 2.5, 0.5)

        st.text('')
        if st.button("Predict type of Iris"):
            result = predict(np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
            species = species_mapping.get(result[0], "Unknown")
            st.text(f"The predicted species is: {species}")

        st.text('')

if __name__ == '__main__':
    main()
