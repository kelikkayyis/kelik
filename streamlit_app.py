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

    # Pilihan halaman dengan tabs
    tab = st.sidebar.radio("Pilih halaman:", ["Iris Data", "Visualisasi", "Prediction", "Analisis"])

    # Halaman untuk Show Data dengan filter
    if tab == "Iris Data":
        st.header("Iris Dataset")

        st.markdown('Dataset bunga Iris, yang dikenal sebagai dataset bunga Iris Fisher, merupakan kumpulan data multivariat yang dipopulerkan oleh Ronald Fisher dalam makalah tahun 1936. Data ini kadang-kadang disebut juga sebagai dataset bunga Iris Anderson karena dikumpulkan oleh Edgar Anderson untuk mengukur variasi morfologis dari tiga spesies Iris terkait. Setiap spesies (Iris setosa, Iris virginica, dan Iris versicolor) memiliki 50 sampel, dengan empat fitur diukur dari masing-masing sampel: panjang dan lebar sepal serta petal, dalam satuan sentimeter. Fisher menggunakan data ini untuk mengembangkan model diskriminan linear yang membedakan spesies berdasarkan fitur-fitur ini, dengan makalahnya diterbitkan dalam Annals of Eugenics (sekarang Annals of Human Genetics).')


        # Pilih spesies untuk visualisasi
        species_tab = st.selectbox(
            "Pilih spesies:",
            options=["All", "Setosa", "Versicolor", "Virginica"],
            index=0
        )
        # species_tab = st.radio("Filter by Species:", options=["All", "Setosa", "Versicolor", "Virginica"])
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
        
    # Visualisasi Species dengan filter
    elif tab == "Visualisasi":
        st.header("Visualisasi Data Iris")
        
        # Pilih spesies untuk visualisasi
        species_option = st.selectbox(
            "Pilih spesies:",
            options=["Setosa", "Versicolor", "Virginica"],
            index=0
        )
        
        # Filter data berdasarkan spesies yang dipilih
        species_data = iris_data[iris_data['species'] == species_option.lower()]

        # Layout untuk scatter plot dan histogram (dua kolom)
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Scatter Plot")
            # Layout untuk scatter plot dan histogram (dua kolom)
            col3, col4 = st.columns(2)

            with col3:
                x_option = st.selectbox(
                    "Pilih kolom untuk sumbu X:",
                    options=species_data.columns[:-1],  # Semua kolom kecuali 'species'
                    index=0
                )
            with col4:
                y_option = st.selectbox(
                    "Pilih kolom untuk sumbu Y:",
                    options=species_data.columns[:-1],  # Semua kolom kecuali 'species'
                    index=1
                )

            fig = px.scatter(
                species_data, 
                x=x_option, 
                y=y_option, 
                color=px.Constant(species_option),
                labels={'color': 'Species'},
                title=f"Scatter Plot {x_option} vs {y_option} for {species_option}"
            )
            
            # Tentukan warna untuk setiap spesies
            if species_option == "Setosa":
                color = 'blue'
            elif species_option == "Versicolor":
                color = 'green'
            else:
                color = 'red'
            
            fig.update_traces(marker=dict(color=color))
            st.plotly_chart(fig)

        with col2:
            st.subheader("Histogram")
            x_option = st.selectbox(
                "Pilih kolom untuk X-Axis:",
                options=species_data.columns[:-1],  # Semua kolom kecuali 'species'
                index=0
            )
            
            fig = px.histogram(
                species_data, 
                x=x_option, 
                nbins=10, 
                title=f"Histogram of {x_option} for {species_option}",
                labels={x_option: x_option, 'count': 'Frequency'}
            )
            fig.update_traces(marker_color=color)
            st.plotly_chart(fig)

    # Prediction Iris Species
    elif tab == "Prediction":
        species_mapping = {
            0: {'name': 'Setosa', 'image': 'images/setosa.jpg'},
            1: {'name': 'Versicolor', 'image': 'images/versicolor.jpg'},
            2: {'name': 'Virginica', 'image': 'images/virginica.jpg'}
        }

        st.title('Prediksi Bunga Iris')
        st.markdown('Machine Learning model untuk memprediksi spesies bunga iris \
             (setosa, versicolor, virginica) berdasarkan sepal/petal \
            dan length/width.')

        col1, col2 = st.columns(2)

        with col1:
            st.text("Sepal characteristics")
            sepal_l = st.slider('Sepal lenght (cm)', 1.0, 8.0, 5.0)
            sepal_w = st.slider('Sepal width (cm)', 2.0, 4.4, 3.0)

        with col2:
            st.text("Petal characteristics")
            petal_l = st.slider('Petal lenght (cm)', 1.0, 7.0, 3.5)
            petal_w = st.slider('Petal width (cm)', 0.1, 2.5, 1.0)

        st.text('')
        if st.button("Predict type of Iris"):
            result = predict(np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
            species_info = species_mapping.get(result[0], {"name": "Unknown", "image": None})
            species_name = species_info['name']
            species_image = species_info['image']
            
            st.text(f"The predicted species is: {species_name}")
            
            if species_image:
                st.image(species_image, caption=f"{species_name} flower", use_column_width=False)
                st.text('')

    # Visualisasi Analysis
    elif tab == "Analisis":
        # Display headers
        st.header("Visualisasi Decision Tree")

        # Load image directly using Streamlit
        image_summary = st.image('decision_tree.png', caption='Decision Tree Visualization', use_column_width=True)

if __name__ == '__main__':
    main()
