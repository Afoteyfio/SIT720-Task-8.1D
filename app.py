
import streamlit as st
import pandas as pd
import joblib

# Loading the saved model
model = joblib.load("random_forest_model.pkl")

st.title("Sydney Housing Price Predictor")

st.write("Enter the property information below to estimate the sale price.")

# Property inputs
suburb = st.selectbox(
    "Suburb",
    ["Blacktown", "Burwood", "Potts Point"]
)

property_type = st.selectbox(
    "Property Type",
    ["Apartment/Unit", "Duplex/Semi-detached", "House",
     "Studio", "Terrace", "Townhouse"]
)

bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10, value=2)
bathrooms = st.number_input("Bathrooms", min_value=0, max_value=10, value=1)
parking = st.number_input("Parking", min_value=0, max_value=10, value=1)

# Predicting the sale price
if st.button("Predict Sale Price"):

    input_data = pd.DataFrame({
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Parking": [parking],
        "Suburb_Blacktown": [int(suburb == "Blacktown")],
        "Suburb_Burwood": [int(suburb == "Burwood")],
        "Suburb_Potts Point": [int(suburb == "Potts Point")],
        "Property_Type_Apartment/Unit": [int(property_type == "Apartment/Unit")],
        "Property_Type_Duplex/Semi-detached": [int(property_type == "Duplex/Semi-detached")],
        "Property_Type_House": [int(property_type == "House")],
        "Property_Type_Studio": [int(property_type == "Studio")],
        "Property_Type_Terrace": [int(property_type == "Terrace")],
        "Property_Type_Townhouse": [int(property_type == "Townhouse")]
    })

    prediction = model.predict(input_data)[0]

    st.write(f"Estimated Sale Price: AUD {prediction:,.0f}")
