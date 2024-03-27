import streamlit as st
import pickle

# Load the model
pkl_path = "../models/XGBoost_Regressor_model.pkl"
with open(pkl_path, "rb") as f:
    model = pickle.load(open("XGBoost_Regressor_model.pkl", "rb"))

# User interface
st.title("My Model App")

# Input fields based on your model's requirements

# income = st.number_input("Enter income:")
cement = st.number_input("Enter cement:")
blast_furnace_slag = st.number_input("Enter blast_furnace_slag:")
fly_ash = st.number_input("Enter fly_ash:")
water = st.number_input("Enter water:")
superplasticizer = st.number_input("Enter superplasticizer:")
age = st.number_input("Enter age:")
# coarse_aggregate = st.number_input("Enter coarse_aggregate:")
# fine_aggregate = st.number_input("Enter fine_aggregate:")


# Preprocess data if needed
data = [cement, blast_furnace_slag, fly_ash, water, superplasticizer,age]

# Make prediction
prediction = model.predict([data])[0]

# Display predictiond
# st.write("Predicted outcome:", prediction)

with st.container():
    st.write("Predicted outcome:", prediction)