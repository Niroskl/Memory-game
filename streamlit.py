import streamlit as st
import pywhatkit as kit
import datetime

st.title("📱 WhatsApp Messenger - Streamlit App")

# הזנת מספר טלפון
phone_number = st.text_input("הכנס מספר טלפון (כולל קידומת מדינה
