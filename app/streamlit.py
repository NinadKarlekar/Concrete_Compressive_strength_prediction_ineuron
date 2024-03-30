import streamlit as st
import pickle
import logging

try:
    # Configure logging (optional, for flexibility and control)
    logging.basicConfig(
        filename="../logs/app_logs.log",  # Customize the filename as needed
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(message)s",
    )

    # Define a function for prediction to encapsulate logic and logging
    def make_prediction(data):
        prediction = model.predict([data])[0]
        logging.info(f"Prediction for data: {data} = {prediction}")
        return prediction

    # Load the model (corrected the file path issue)
    with open("../models/XGBoost_Regressor_model.pkl", "rb") as f:
        model = pickle.load(f)

    # User interface with CSS styling
    st.set_page_config(page_title="My Model App", layout="wide")  # Adjust layout as needed

    # Define CSS styles (create a separate CSS file if desired)
    body_style = """
    body {
        background-image: url("img\c1.png"");  # Replace with your image path
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        font-family: Arial, sans-serif;  # Optional font styling
    }
    """

    st.markdown(f"<style>{body_style}</style>", unsafe_allow_html=True)

    # Title and input fields
    st.title("My Model App")

    cement = st.number_input("Enter cement:")
    blast_furnace_slag = st.number_input("Enter blast_furnace_slag:")
    fly_ash = st.number_input("Enter fly_ash:")
    water = st.number_input("Enter water:")
    superplasticizer = st.number_input("Enter superplasticizer:")
    age = st.number_input("Enter age:")

    logging.info(
        f"User input: cement={cement}, blast_furnace_slag={blast_furnace_slag}, fly_ash={fly_ash}, water={water}, superplasticizer={superplasticizer}, age={age}"
    )

    # Preprocess data if needed
    data = [cement, blast_furnace_slag, fly_ash, water, superplasticizer, age]

    # Make prediction and display results
    logging.info("Model XGBoost_Regressor_model.pkl loaded successfully")

    prediction = model.predict([data])[0]
    logging.info(f"Predicted outcome for data {data}: {prediction}")

    with st.container():
        st.write("Predicted outcome:", prediction)

    logging.info('-' * 80)  # Creates a line of 80 dashes

except Exception as e:
    logging.error(f"An error occurred: {e}")
