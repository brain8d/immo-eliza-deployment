import requests
import streamlit as st

# The URL of your FastAPI endpoint
url = "https://immo-eliza-deployment-20bn.onrender.com/predict"

# Streamlit app title
st.title("Real Estate Price Prediction")

#sylvan Order:

col1, col2 = st.columns(2)

with col1:
    subproperty_type = st.selectbox("Subproperty Type", ("APARTMENT","APARTMENT_BLOCK","BUNGALOW","CASTLE","CHALET","COUNTRY_COTTAGE","EXEPTIONAL_PROPERTY", "DUPLEX","FARMHOUSE", "FLAT_STUDIO","GROUND_FLOOR","LOFT","KOT","MANOR_HOUSE","MANSION","MIXED_USE_BUILDING","PENTHOUSE","SERVICE_FLAT","TOWN_HOUSE","TRIPLEX","VILLA", "HOUSE","OTHER_PROPERTY"))
    state_building = st.selectbox("Building State", ("MISSING","AS_NEW","GOOD","JUST_RENOVATED","TO_RESTORE","TO_RENOVATE","TO_BE_DONE_UP"))
    locality = st.selectbox("Locality", ("Aalst","Antwerp","Arlon","Ath","Bastogne","Brugge","Brussels","Charleroi","Dendermonde","Diksmuide","Dinant","Eeklo","Gent","Halle-Vilvoorde","Hasselt","Huy","Ieper","Kortrijk","Leuven","Liège","Maaseik","Marche-en-Famenne","Mechelen","Mons","Mouscron","Namur","Neufchâteau","Nivelles","Oostend","Oudenaarde","Philippeville","Roeselare","Sint-Niklaas","Soignies","Thuin","Tielt","Tongeren","Tournai","Turnhout","Verviers","Veurne","Virton","Waremme"))
    zip_code = st.number_input("ZIP Code", value=1000, format="%d")
    construction_year = st.number_input("Construction Year", value=2000, min_value=1800, max_value=2024)
    total_area_sqm = st.number_input("Total Area in sqm", value=10,min_value=10,max_value=15000)
    nbr_bedrooms = st.number_input("Number of Bedrooms", value=2, min_value=1, max_value=100)
    equipped_kitchen = st.selectbox("Equipped Kitchen", ("MISSING", "INSTALLED", "HYPER_EQUIPPED","SEMI_EQUIPPED","NOT_INSTALLED","USA_UNINSTALLED","USA_HYPER_EQUIPPED","USA_SEMI_EQUIPPED",))
    



with col2:
   
    surface_land_sqm = st.number_input("Land Area in sqm", value=150, min_value=10, max_value=1000000)
    nbr_frontages = st.number_input("Number of Frontages", value=0, min_value=0, max_value=10)
    epc = st.selectbox("Energy Performance Certificate", ("MISSING", "A","B","C","D","E","F"))
    fl_double_glazing = st.checkbox("Double Glazing", value=True)  
    fl_open_fire = st.checkbox("Open Fire")  
    fl_terrace = st.checkbox("Terrace")
    if fl_terrace:
        terrace_sqm = st.number_input("Terrace Area in sqm", value=10, min_value=10, max_value=500)
    else :
        terrace_sqm = 0
    fl_garden = st.checkbox("Garden")
    if fl_garden:
        garden_sqm = st.number_input("Garden Area in sqm", value=10, min_value=10, max_value=1000000)
    else:
        garden_sqm = 0

    fl_swimming_pool = st.checkbox("Swimming Pool")
    
   




    # Input manualy this
    latitude = 0
    longitude = 0
    primary_energy_consumption_sqm = 0
    cadastral_income = 0

    # Input fields for the flag features


    

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
