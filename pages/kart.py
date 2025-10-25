import streamlit as st
from pages import Products
def show_kart(Model,image):
        st.markdown(f"### {Model}")
        st.image(image)
        
        

if Products.st.session_state.kart != []:
            
           
    for i in range(len(Products.st.session_state.kart)):
                show_kart(Products.st.session_state.kart[i][0],Products.st.session_state.kart[i][1])
                        
else:
    st.error("No items in the kart yet!")