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
    st.set_page_config(page_title="Concrete Compressive Strength", layout="wide")  # Adjust layout as needed

    # Define CSS styles (create a separate CSS file if desired)
    body_style = """
    body {
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        font-family: Arial, sans-serif;  # Optional font styling
    }
    """

    st.markdown(f"<style>{body_style}</style>", unsafe_allow_html=True)

    # Title and input fields
    st.title("Concrete Compressive Strength")

    cement = st.number_input("Enter the amount of Cement (component 1) in kg per m³ mixture:")
    blast_furnace_slag = st.number_input(
        "Enter the amount of Blast Furnace Slag (component 2) in kg per m³ mixture:"
    )
    fly_ash = st.number_input("Enter the amount of Fly Ash (component 3) in kg per m³ mixture:")
    water = st.number_input("Enter the amount of Water (component 4) in kg per m³ mixture:")
    superplasticizer = st.number_input(
        "Enter the amount of Superplasticizer (component 5) in kg per m³ mixture:"
    )
    age = st.number_input("Enter the Age of the concrete (days, 1-365):")


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
        st.write(
            "Predicted compressive strength of the concrete mixture:",
            f"{prediction:.2f} MPa",  # Format prediction with 2 decimal places
        )


    logging.info('-' * 80)  # Creates a line of 80 dashes

except Exception as e:
    logging.error(f"An error occurred: {e}")
