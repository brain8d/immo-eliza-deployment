import pandas as pd


def body(data):
    if data["property_type"].empty:
        data["property_type"] = "MISSING"
    if data["subproperty_type"].empty:
        data["subproperty_type"] = "MISSING"
    if data["region"].empty:
        data["region"] = "MISSING"
    if data["province"].empty:
        data["province"] = "MISSING"
    if data["locality"].empty:
        data["locality"] = "MISSING"
    if data["zip_code"].empty:
        data["zip_code"] = "MISSING"
    if data["latitude"].empty:
        data["latitude"] = None
    if data["longitude"].empty:
        data["longitude"] = None
    if data["total_area_sqm"].empty:
        data["total_area_sqm"] = None
    if data["surface_land_sqm"].empty:
        data["surface_land_sqm"] = None
    if data["nbr_frontages"].empty:
        data["nbr_frontages"] = None
    if data["nbr_bedrooms"].empty:
        data["nbr_bedrooms"] = 0
    if data["equipped_kitchen"].empty:
        data["equipped_kitchen"] = "MISSING"
    if data["fl_furnished"].empty:
        data["fl_furnished"] = 0
    if data["fl_open_fire"].empty:
        data["fl_open_fire"] = 0
    if data["fl_terrace"].empty:
        data["fl_terrace"] = 0
    if data["terrace_sqm"].empty:
        data["terrace_sqm"] = None
    if data["fl_garden"].empty:
        data["fl_garden"] = 0
    if data["garden_sqm"].empty:
        data["garden_sqm"] = 0
    if data["fl_swimming_pool"].empty:
        data["fl_swimming_pool"] = 0
    if data["fl_floodzone"].empty:
        data["fl_floodzone"] = 0
    if data["state_building"].empty:
        data["state_building"] = "MISSING"
    if data["primary_energy_consumption_sqm"].empty:
        data["primary_energy_consumption_sqm"] = None
    if data["epc"].empty:
        data["epc"] = "MISSING"
    if data["heating_type"].empty:
        data["heating_type"] = "MISSING"
    if data["fl_double_glazing"].empty:
        data["fl_double_glazing"] = 0
    if data["cadastral_income"].empty:
        data["cadastral_income"] = None

    print(data)
    return data


if __name__ == "__main__":

    data = pd.read_csv("immo-eliza-deployment\data\properties_small.csv")
    body(data)
