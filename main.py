# -*- coding: utf-8 -*-
"""
Created on Tue Jul 7 10:57:29 2026

@author: gudap
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle

# Create FastAPI app
app = FastAPI()

# Load trained model
with open("diabetes_model.sav", "rb") as file:
    diabetes_model = pickle.load(file)


# Input schema
class ModelInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


# Home route
@app.get("/")
def home():
    return {"message": "Diabetes Prediction API is Running Successfully!"}


# Prediction route
@app.post("/diabetes_prediction")
def diabetes_prediction(input_data: ModelInput):

    input_list = [
        input_data.Pregnancies,
        input_data.Glucose,
        input_data.BloodPressure,
        input_data.SkinThickness,
        input_data.Insulin,
        input_data.BMI,
        input_data.DiabetesPedigreeFunction,
        input_data.Age,
    ]

    prediction = diabetes_model.predict([input_list])

    if prediction[0] == 0:
        result = "The person is not diabetic"
    else:
        result = "The person is diabetic"

    return {
        "prediction": int(prediction[0]),
        "result": result
    }