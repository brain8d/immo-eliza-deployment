# from app.model.model import predict_pipeline
# from app.model.model import version as model_version

import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, List, Union

app = FastAPI()

# Load model and artifacts once during startup
artifacts = joblib.load("model/Gradient_boost_artifacts.joblib")
imputer = artifacts["imputer"]
enc = artifacts["enc"]
model = artifacts["model"]

# Features class


class Features(BaseModel):
    num_features: Dict[str, float]
    fl_features: Dict[str, int]
    cat_features: Dict[str, str]

# Check function


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Immo Eliza ML model API!"}

# Predict function


@app.post("/predict")
async def predict(features: Features):
    # Convert features to DataFrame
    data_df = pd.DataFrame([features.features])

    # Separate numerical and categorical features based on artifacts
    num_features = [
        f for f in data_df.columns if f in artifacts["features"]["num_features"]]
    fl_features = [
        f for f in data_df.columns if f in artifacts["features"]["fl_features"]]
    cat_features = [
        f for f in data_df.columns if f in artifacts["features"]["cat_features"]]

    # Process numerical features
    if num_features:
        data_df[num_features] = imputer.transform(data_df[num_features])

    # Process categorical features
    if cat_features:
        data_cat = enc.transform(data_df[cat_features]).toarray()
        data_df.drop(cat_features, axis=1, inplace=True)
        cat_df = pd.DataFrame(data_cat, columns=enc.get_feature_names_out())
        data_df = pd.concat([data_df, cat_df], axis=1)

    # Make predictions
    predictions = model.predict(data_df)

    return {"predictions": predictions.tolist()}
