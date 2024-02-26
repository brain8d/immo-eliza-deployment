import pandas as pd
import streamlit as st
import json
import requests


st.title("House price predictor by MerMade")

option = st.selectbox(
    'What type of subproperty?',
    ("Apartment", "House"))

option = st.selectbox(
    'How many bedrooms?',
    (1, 2, 3, 4, 5, "6+"))

st.write('You selected:', option)







data_df = pd.DataFrame(
    {
        "Price Range": [20, 950, 250, 500],
    }
)

st.data_editor(
    data_df,
    column_config={
        "Price Range": st.column_config.NumberColumn(
            "Price (in Euros)",
            help="The price of your future home",
            min_value=0,
            max_value=1000,
            step=1,
            format="€%d",
        )
    },
    hide_index=True,
)