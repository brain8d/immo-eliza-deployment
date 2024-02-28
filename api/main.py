import joblib
import numpy as np
import pandas as pd
import sklearn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Dict

app = FastAPI()

DEFAULTS = {
    "num_features": {
        "construction_year": 1984,
        "latitude": 50.88,
        "longitude": 4.33,
        "total_area_sqm": 163.67,
        "surface_land_sqm": 1157,
        "nbr_frontages": 2.80,
        "nbr_bedrooms": 2.79,
        "terrace_sqm": 11.58,
        "primary_energy_consumption_sqm": 250,
        "cadastral_income": 1885.94,
        "garden_sqm": 115.64,
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
        "locality": "MISSING",
        "equipped_kitchen": "MISSING",
        "state_building": "MISSING",
        "epc": "MISSING"
    }
}

# Load model and artifacts once during startup
artifacts = joblib.load("model/Gradient_boost_artifacts.joblib")
imputer = artifacts["imputer"]
enc = artifacts["enc"]
model = artifacts["model"]

# Features class
class Features(BaseModel):
    num_features: Dict[str, float] = Field(
        default=DEFAULTS["num_features"],
        example={"zip_code": 1000},
        description="Numerical features with their default values."
    )
    fl_features: Dict[str, int] = Field(
        default=DEFAULTS["fl_features"],
        example={"fl_garden": 1},
        description="Flag features with their default values."
    )
    cat_features: Dict[str, str] = Field(
        default=DEFAULTS["cat_features"],
        example={"epc": "A"},
        description="Categorical features with their default values."
    )

# Check function
@app.get("/")
async def read_root():
    return {"message": "Immo Eliza ML model API is alive!"}

# Predict function
@app.post("/predict")
async def predict(features: Features):
    # Fill in missing values with defaults
    filled_features = {
        "num_features": {**DEFAULTS["num_features"], **features.num_features},
        "fl_features": {**DEFAULTS["fl_features"], **features.fl_features},
        "cat_features": {**DEFAULTS["cat_features"], **features.cat_features},
    }
    
    # Now proceed with constructing DataFrame from filled_features
    num_df = pd.DataFrame([filled_features["num_features"]])
    fl_df = pd.DataFrame([filled_features["fl_features"]])
    cat_df = pd.DataFrame([filled_features["cat_features"]])

    # Process numerical features with imputer
    num_df = pd.DataFrame(imputer.transform(num_df), columns=num_df.columns)

    # Process categorical features with encoder
    if not cat_df.empty:
        cat_encoded = enc.transform(cat_df).toarray()
        cat_df = pd.DataFrame(cat_encoded, columns=enc.get_feature_names_out())

    # Combine all features
    data_df = pd.concat([num_df, fl_df, cat_df], axis=1)

    # Make predictions
    predictions = model.predict(data_df)
    predicted_value = predictions.tolist()[0]

    # Use model's performance to set range of predicted price
    MAE = 80000
    lower_bound = predicted_value - MAE
    upper_bound = predicted_value + MAE

    return {
        "Prediction of price": f"€ {predicted_value:.0f}",
        "Price range based on model accuracy": f"€ {lower_bound:.0f} - € {upper_bound:.0f}"
    }