import time
import streamlit as st
import pandas as pd


if "kart" not in st.session_state:
    
    st.session_state.kart=[]





df=pd.read_csv("watches_dataset.csv")
df=df.fillna(value="Description not added yet")

@st.dialog("Casio Watch")

def full_view(Company,Model,Price,Notes,image):
    st.image(image)
    st.write(f"Model:{Model}")
    st.write(f"Company:{Company}")
    st.write(f"Price:{Price}")
    st.markdown(f"**Description**")
    st.write(Notes)
    col1,col2=st.columns(2)
    with col1:
        st.button("Buy now")
    
    with col2:
        if st.button("Add to kart"):
            
            st.session_state.kart.append([Model,image])
            
            


if __name__ == "__main__":

    st.markdown("## **Products**")
    
    
    st.image("001_8a65959a.jpg")

    if st.button("Details","button_a"):
        
        full_view("Casio",df.iat[0,4],df.iat[0,2],df.iat[0,6],"001_8a65959a.jpg")
        

    st.image("003_77c3ca09.jpg")
    if st.button("Details","button_b"):
        full_view("Casio",df.iat[1,4],df.iat[1,2],df.iat[1,6],"003_77c3ca09.jpg")

    st.image("005_a545cc1a.jpg")
    if st.button("Details","button_c"):
        full_view("Casio",df.iat[2,4],df.iat[2,2],df.iat[2,6],"005_a545cc1a.jpg")

    st.image("006_26bab30f.jpg")
    if st.button("Details","button_d"):
        full_view("Casio",df.iat[3,4],df.iat[3,2],df.iat[3,6],"006_26bab30f.jpg")

    st.image("007_003ebd8c.jpg")
    if st.button("Details","button_e"):
        full_view("Casio",df.iat[4,4],df.iat[4,2],df.iat[4,6],"007_003ebd8c.jpg")

    st.image("008_1c061100.jpg")
    if st.button("Details","button_f"):
        full_view("Casio",df.iat[5,4],df.iat[5,2],df.iat[5,6],"008_1c061100.jpg")

    st.image("009_c04c6b85.jpg")
    if st.button("Details","button_g"):
        full_view("Casio",df.iat[6,4],df.iat[6,2],df.iat[6,6],"009_c04c6b85.jpg")

    st.image("010_eb22bd2f.jpg")
    if st.button("Details","button_h"):
        full_view("Casio",df.iat[7,4],df.iat[7,2],df.iat[7,6],"010_eb22bd2f.jpg")

    st.image("024_9883bd9f.jpg")
    if st.button("Details","button_i"):
        full_view("Casio",df.iat[8,4],df.iat[8,2],df.iat[8,6],"024_9883bd9f.jpg")

    st.image("026_a0da3370.jpg")
    if st.button("Details","button_j"):
        full_view("Casio",df.iat[9,4],df.iat[9,2],df.iat[9,6],"026_a0da3370.jpg")