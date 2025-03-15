import streamlit as st
from src.fraud_detection_pipeline import detect_fraud

st.title("Fraud Detection System")
transaction = st.text_input("Enter transaction details:")
if st.button("Check for Fraud"):
    result = detect_fraud(transaction)
    st.write("🚨 FRAUD ALERT!" if result.all().all() else "✅ Safe Transaction")

