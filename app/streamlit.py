import streamlit as st
import pickle

# Load the model
pkl_path = "./XGBoost_Regressor_model.pkl"
with open(pkl_path, "rb") as f:
    model = pickle.load(open("XGBoost_Regressor_model.pkl", "rb"))

# User interface
st.title("My Model App")

# Input fields based on your model's requirements
age = st.number_input("Enter age:")
income = st.number_input("Enter income:")

# Preprocess data if needed
data = [age, income]

# Make prediction
prediction = model.predict([data])[0]

# Display prediction
st.write("Predicted outcome:", prediction)
