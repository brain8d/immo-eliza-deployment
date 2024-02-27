import pandas as pd
import streamlit as st
import json
import requests


st.title("How much is your home worth?")
st.text("House price predictor by MerMade")

subproperty = st.selectbox(
    'What type of subproperty?',
    ("Apartment", "House"))

option = st.selectbox(
    'How many bedrooms?',
    (1, 2, 3, 4, 5, "6+"))



## Testing other visualization method
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


##----- Pseudo code 

# dict_api = {
#     param1: subproperty
# }

# r = request.get(dict_api, URL API)

# json.load(r)

