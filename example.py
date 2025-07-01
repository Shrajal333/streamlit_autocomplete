import streamlit as st
from streamlit_autocomplete import st_textcomplete_autocomplete

city_names = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "London",
    "Paris", "Berlin", "Tokyo", "Mumbai", "Delhi", 
    "Bangalore", "Chennai", "Kolkata", "Sydney", "Melbourne",
    "Toronto", "Vancouver", "Dubai", "Singapore", "Bangkok",
    "Hong Kong", "Shanghai", "Istanbul", "Moscow", "Cape Town"
]

query = st_textcomplete_autocomplete(
    label="Enter city or metric",
    options=city_names,
    key="city_autocomplete",
    help="Start typing a city name"
)

st.write("You typed:", query)