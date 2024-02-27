import requests

# The URL of your FastAPI endpoint
url = "http://localhost:8000/predict"

# The structured request payload
payload = {
    "num_features": {
        "construction_year": 2000,
        "latitude": 50.8503,
        "longitude": 4.3517,
        "total_area_sqm": 100.0,
        "surface_land_sqm": 500.0,
        "nbr_frontages": 2.0,
        "nbr_bedrooms": 3.0,
        "terrace_sqm": 10.0,
        "primary_energy_consumption_sqm": 250.0,
        "cadastral_income": 1000.0,
        "garden_sqm": 50.0,
        "zip_code": 1000
    },
    "fl_features": {
        "fl_terrace": 0,
        "fl_open_fire": 0,
        "fl_swimming_pool": 0,
        "fl_garden": 0,
        "fl_double_glazing": 1
    },
    "cat_features": {
        "subproperty_type": "APARTMENT",
        "locality": "Brussels",
        "equipped_kitchen": "NOT_INSTALLED",
        "state_building": "TO_RENOVATE",
        "epc": "MISSING"
    }
}

# Sending the POST request to your FastAPI endpoint
response = requests.post(url, json=payload)

# Print out the response to see the prediction
#print(response.json())

# Check if the response is successful
if response.status_code == 200:
    # Print out the CSV response directly
    print(response.text)  # Prints the CSV formatted text directly to the console
else:
    # Handle errors
    print(f"Failed to get response: {response.status_code}")
    print(response.text)