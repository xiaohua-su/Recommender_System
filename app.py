import streamlit as st
import pandas as pd



st.title("Hello World")

st.write("## This is a real app!")

genre = st.multiselect("Movie Genre",
    options=['comdedy', 'action'])

st.write(f'you like {genre}')

num_recommendations = st.number_input("How many recommendations would you like?", min_value=0, max_value=10)

st.write(f'you like {num_recommendations} of {genre} movies')