import streamlit as st
from maps import maps

property_type = st.selectbox("Property Type", ["house", "apartment"])

num_rooms = st.selectbox(
    "Number of rooms",
    list(range(1, 10)),  # This will create a list with numbers from 1 to 9
)

street_name = st.text_input("Street Name")

postal_code = st.selectbox(
    "Postal Code",
    list(range(1000, 10000)),  # This will create a list with numbers from 1000 to 9999
)

city = st.text_input("City")

living_space = st.slider(
    "Living Space (in square meters)",
    min_value=10,
    max_value=900,
    value=450,  # This sets the default value
)

st.write(
    "You selected a",
    property_type,
    "with",
    num_rooms,
    "rooms, located at",
    street_name,
    postal_code,
    city,
    "with a living space of",
    living_space,
    "square meters",
)

if st.button("See on Map"):
    st.write(maps(1083)) 
