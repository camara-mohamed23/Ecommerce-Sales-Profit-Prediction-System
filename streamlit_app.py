import streamlit as st
import joblib
import pandas as pd

st.title("EcomInsightAI - Profit Prediction")

model = joblib.load("models/trained_model.pkl")

quantity = st.number_input("Quantity", min_value=1, value=1)
year = st.number_input("Year", min_value=2022, max_value=2030, value=2024)
month = st.number_input("Month", min_value=1, max_value=12, value=1)
revenue_per_unit = st.number_input("Revenue per Unit", min_value=1.0, value=100.0)

if st.button("Predict Profit"):
    input_data = pd.DataFrame(
        [[quantity, year, month, revenue_per_unit]],
        columns=["Quantity", "Year", "Month", "Revenue_per_Unit"]
    )

    prediction = model.predict(input_data)
    st.success(f"Predicted Profit: {prediction[0]:.2f}")