import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Set page title
st.set_page_config(page_title="Insurance Charges Prediction", layout="centered")

# Load your trained model (update the filename if needed)
model_path = "insurance_model.pkl"  # Replace with your model file
try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Please upload your trained model (insurance_model.pkl).")
    st.stop()

# App title
st.title("🩺 Insurance Charges Prediction App")
st.write("Estimate medical insurance charges based on user details.")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=25)
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0)
smoker = st.selectbox("Do you smoke?", ("No", "Yes"))

# Convert input into dataframe for prediction
smoker_yes = 1 if smoker == "Yes" else 0
input_data = pd.DataFrame({
    'age': [age],
    'bmi': [bmi],
    'smoker_yes': [smoker_yes]
})

# Prediction
if st.button("Predict Charges"):
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Insurance Charge: **${prediction[0]:,.2f}**")

# Footer
st.write("---")
st.caption("Developed by Mansi Madrewar | Linear Regression Model")

