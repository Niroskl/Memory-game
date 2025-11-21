import streamlit as st
import random
import pyttsx3

st.set_page_config(page_title="מה יש לאכול?", layout="wide")
st.title("🤖 המחשב אומר מה יש לאכול! 🍽️")
st.write("לחץ על הכפתור והמחשב יגיד בקול מה יש לאכול היום!")

# רשימת מאכלים
foods = ["תפוח 🍎", "בננה 🍌", "המבורגר 🍔", "פיצה 🍕", "סושי 🍣", 
         "עוגיה 🍪", "סלט 🥗", "נקניקיה 🌭", "לחם 🥖", "דונאט 🍩"]

# אתחול היסטוריה
if "history" not in st.session_state:
    st.session_state.history = []

# Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # מהירות הדיבור

# כפתור שהמחשב מדבר
if st.button("🤖 מה יש לאכול היום?"):
    choice = random.choice(foods)
    st.session_state.history.append(choice)
    st.success(f"המחשב אומר: {choice}!")
    
    # המחשב מדבר
    engine.say(f"היום
