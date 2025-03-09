import streamlit as st
import requests
import json
st.header('Market Price Prediction App')
neighborhood_list = [
    'central',
    'other']

neighborhood = st.selectbox(label='Select Neighborhood', options=neighborhood_list)

ap_size = st.number_input(
    label='Size in square metres',
    min_value=30,
    max_value=100,
    value=50)
nr_room = st.number_input(
    label='Number of rooms',
    min_value=2,
    max_value=4)
nr_bathroom = st.number_input(
    label='Number of bathrooms',
    min_value=1,
    max_value=4,
    value=2
)
year_built = st.number_input(
    label='Year built',
    min_value=1985,
    max_value=2024,
    value=2000)
# prediction button
calculate = st.button(label='Calculate Price')
if calculate:
    input_data = {
        "rooms": nr_room,
        "size": ap_size,
        "bathrooms": nr_bathroom,
        "neighbourhood": neighborhood,
        "year_built": year_built
    }
    url = st.secrets["API_URL"]
    result = requests.post(url, json=input_data)
    st.write(f"### {result.json()['price']} Euro")

