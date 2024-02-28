import requests
import streamlit as st

# The URL of your FastAPI endpoint
# url = "https://immo-eliza-deployment-20bn.onrender.com/predict"

url = st.secrets["api_url"]


# Streamlit app title
st.title("Real Estate Price Prediction")
st.text("by MerMade")

# Input fields for the numeric features
construction_year = st.number_input("Construction Year", value=2000, min_value=1900, max_value=2024)
latitude = st.number_input("Latitude", value=50.8503)
longitude = st.number_input("Longitude", value=4.3517)
total_area_sqm = st.number_input("Total Area in sqm", value=100.0)
surface_land_sqm = st.number_input("Land Area in sqm", value=500.0)
nbr_frontages = st.number_input("Number of Frontages", value=0, min_value=0)
nbr_bedrooms = st.number_input("Number of Bedrooms", value=3.0, min_value=0.0)
terrace_sqm = st.number_input("Terrace Area in sqm", value=10.0)
primary_energy_consumption_sqm = st.number_input("Primary Energy Consumption in kWh/sqm", value=250.0)
cadastral_income = st.number_input("Cadastral Income", value=1000.0)
garden_sqm = st.number_input("Garden Area in sqm", value=50.0)
zip_code = st.number_input("ZIP Code", value=1000, format="%d")

# Input fields for the flag features
fl_terrace = st.checkbox("Terrace")
fl_open_fire = st.checkbox("Open Fire")
fl_swimming_pool = st.checkbox("Swimming Pool")
fl_garden = st.checkbox("Garden")
fl_double_glazing = st.checkbox("Double Glazing", value=True)

# Dropdown for categorical features
subproperty_type = st.selectbox("Subproperty Type", ("APARTMENT", "HOUSE"))
locality = st.text_input("Locality", "Brussels")
equipped_kitchen = st.selectbox("Equipped Kitchen", ("NOT_INSTALLED", "SEMI_EQUIPPED", "INSTALLED"))
state_building = st.selectbox("Building State", ("TO_RENOVATE", "TO_REBUILD"))
epc = st.selectbox("Energy Performance Certificate", ("MISSING", "A"))

# Button to send the request
if st.button("Predict Price"):
    payload = {
        "num_features": {
            "construction_year": construction_year,
            "latitude": latitude,
            "longitude": longitude,
            "total_area_sqm": total_area_sqm,
            "surface_land_sqm": surface_land_sqm,
            "nbr_frontages": nbr_frontages,
            "nbr_bedrooms": nbr_bedrooms,
            "terrace_sqm": terrace_sqm,
            "primary_energy_consumption_sqm": primary_energy_consumption_sqm,
            "cadastral_income": cadastral_income,
            "garden_sqm": garden_sqm,
            "zip_code": zip_code
        },
        "fl_features": {
            "fl_terrace": int(fl_terrace),
            "fl_open_fire": int(fl_open_fire),
            "fl_swimming_pool": int(fl_swimming_pool),
            "fl_garden": int(fl_garden),
            "fl_double_glazing": int(fl_double_glazing)
        },
        "cat_features": {
            "subproperty_type": subproperty_type,
            "locality": locality,
            "equipped_kitchen": equipped_kitchen,
            "state_building": state_building,
            "epc": epc
        }
    }

    print(payload)
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        # Display the prediction result
        prediction = response.text
        st.success(f"Predicted Price: {prediction}")
    else:
        # Handle errors
        st.error(f"Failed to get response: {response.status_code}")
        print(response.text)
