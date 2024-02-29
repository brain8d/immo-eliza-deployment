import requests
import streamlit as st
import pandas as pd
from maps import maps
#from streamlit_folium import folium_static

# Secret key for API adress
url = st.secrets["api_url"]

# Streamlit app title

st.markdown("<h1 style='text-align: center;'>Real Estate Price Prediction</h1><br>", unsafe_allow_html=True)


dataLocality = pd.read_csv("data/locality_zip_codes.csv")


#sylvan Order:

col1, col2 = st.columns(2)

with col1:
    subproperty_type = st.selectbox("Subproperty Type", ("APARTMENT",))
    locality = st.selectbox("Locality", ("Aalst","Antwerp","Arlon","Ath","Bastogne","Brugge","Brussels","Charleroi","Dendermonde","Diksmuide","Dinant","Eeklo","Gent","Halle-Vilvoorde","Hasselt","Huy","Ieper","Kortrijk","Leuven","Liège","Maaseik","Marche-en-Famenne","Mechelen","Mons","Mouscron","Namur","Neufchâteau","Nivelles","Oostend","Oudenaarde","Philippeville","Roeselare","Sint-Niklaas","Soignies","Thuin","Tielt","Tongeren","Tournai","Turnhout","Verviers","Veurne","Virton","Waremme"))
    if locality:
        data = dataLocality[dataLocality['locality'] == f"{locality}"]
        zip_code = st.selectbox("ZIP Code",data['zip_code'].to_list())   
    construction_year = st.number_input("Construction Year", value=2000, min_value=1800, max_value=2024)
    total_area_sqm = st.number_input("Total Area in sqm", value=150,min_value=10,max_value=1000)
    epc = st.selectbox("Energy Performance Certificate", ("MISSING", "A","B","C","D","E","F"))
    nbr_bedrooms = st.slider("Number of Bedrooms", value=3, min_value=1, max_value=10)
    nbr_frontages = st.slider("Number of Frontages", value=1, min_value=0, max_value=5)

with col2:
    surface_land_sqm = st.slider("Land Area in sqm", value=150, min_value=10, max_value=1000)
    
    fl_double_glazing = st.checkbox("Double Glazing")  
    fl_open_fire = st.checkbox("Open Fire")  
    fl_swimming_pool = st.checkbox("Swimming Pool")
    equipped_kitchen = st.checkbox("Equipped Kitchen")
    state_building = st.checkbox("Building State")
    fl_terrace = st.checkbox("Terrace", value=True)
    if fl_terrace:
        terrace_sqm = st.slider("Terrace Area in sqm", value=20, min_value=10, max_value=100)
    else :
        terrace_sqm = 0
    fl_garden = st.checkbox("Garden", value=True)
    if fl_garden:
        garden_sqm = st.slider("Garden Area in sqm", value=80, min_value=10, max_value=1000)
    else:
        garden_sqm = 0

 
    

# Input manualy this
#latitude = 0
#longitude = 0
#primary_energy_consumption_sqm = 0
#cadastral_income = 0
payload = {
        "num_features": {
            "construction_year": construction_year,
            #"latitude": latitude,
            #"longitude": longitude,
            "total_area_sqm": total_area_sqm,
            "surface_land_sqm": surface_land_sqm,
            "nbr_frontages": nbr_frontages,
            "nbr_bedrooms": nbr_bedrooms,
            "terrace_sqm": terrace_sqm,
            #"primary_energy_consumption_sqm": primary_energy_consumption_sqm,
            #"cadastral_income": cadastral_income,
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
            "property_type": subproperty_type,
            "locality": locality,
            "kitchen_clusterized": "Yes" if equipped_kitchen else "No",
            "state_building_clusterized": "Yes" if state_building else "No",
            "epc": epc
        }
    }


col1, col2, col3, col4 = st.columns([1,2,1,1])
with col2:

    # Button to send the request
    if st.button("Predict Price"):
        
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            # Display the prediction result
            prediction = response.text
            st.success(f"Predicted Price: {prediction}")
                
        else:
            # Handle errors
            st.error(f"Failed to get response: {response.status_code}")
            print(response.text)

with col3:
    see_map = st.button("See on Map")

if see_map:
    folium_static(maps(zip_code,total_area_sqm,subproperty_type))
    #st.map(maps(zip_code))  
    st.markdown("""
    <div style="text-align: center;">
        <h4>Legenda</h4>
        <i class="fa fa-building" style="color:black"></i> Apartments <br>
        <i class="fa fa-house" style="color:black"></i> Houses <br>
        <i class="fa fa-map-marker" style="color:blue"></i> <= 200k <br>
        <i class="fa fa-map-marker" style="color:green"></i> > 200k and <= 400k <br>
        <i class="fa fa-map-marker" style="color:orange"></i> > 400k and <= 600k <br>
        <i class="fa fa-map-marker" style="color:red"></i> > 600k and <= 800k <br>
        <i class="fa fa-map-marker" style="color:black"></i> > 800k <br>
    </div>
    """, unsafe_allow_html=True)
    

    