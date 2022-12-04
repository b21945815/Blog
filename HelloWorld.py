import streamlit as st
header = st.container()
usingModel = st.container()
with header:
    st.title("Looking for predictions of cars' price")
    st.text("This is just a extra line to show you the difference between these functions")
with usingModel:
    st.title("Input to estimate the cars' price")
