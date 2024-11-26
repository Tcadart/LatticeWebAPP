import streamlit as st
from Lattice_generator import *
from Design_Explorer_Hybrid import *

st.set_page_config(layout="wide")

# Ajouter le menu de navigation
page = st.sidebar.selectbox(
    "Navigation",
    ["Lattice Generator", "Design Explorer Lattice Hybrid"]
)

# Appeler la fonction correspondante
if page == "Lattice Generator":
    lattice_generator_page()
elif page == "Design Explorer Lattice Hybrid":
    Design_Explorer_Hybrid()
