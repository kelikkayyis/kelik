import streamlit as st 

def main() : 
    #sidebar 
    sidebar_checkbox = st.sidebar.checkbox('Checkbox di Sidebar')
    sidebar_radio_button = st.sidebar.radio('Pilih Menu',options=['A','B','C'])
    
    #columns :
    col1, col2, col3 = st.columns(3)

    with col1:
       st.header("A cat")
       st.image("https://static.streamlit.io/examples/cat.jpg")
    #atau dengan assignment 
    image_col1 = col1.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
       st.header("A dog")
       st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
       st.header("An owl")
       st.image("https://static.streamlit.io/examples/owl.jpg")
    #expander 
    #dengan with atau dengan assignment 
    expander = st.expander("Klik Untuk Detail ")
    expander.write('Anda Telah Membuka Detail')
    
if __name__ == '__main__' : 
  main()
