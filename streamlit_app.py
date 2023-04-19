import streamlit as st

st.write(
"""
Compare 3 Numbers
"""
)
a = st.number_input("First Number")
b = st.number_input("Second Number")
c = st.number_input("Third Number")

st.write(a,b,c)
