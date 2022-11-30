import streamlit as st
header = st.container()
dataset = st.container()
with header:
    st.title("Welcome to My Blog")
    st.text("Hello world");
with dataset:
    st.title("Data on cars' price")
