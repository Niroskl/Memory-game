import streamlit as st
from transformers import pipeline
from PIL import Image
import random

st.set_page_config(page_title="🤖 רובוטים חכמים", layout="wide")
st.title("🤖 רובוטים חכמים - Streamlit Game")

# רובוטים עם תמונה מותאמת
robots = {
    "רובוט דובר": "robot_speaker.png",
    "רובוט מנקה": "robot_cleaner.png",
    "רובוט שמירה": "robot_guard.png",
    "רובוט עוזר": "robot_helper.png"
}

# Text Generation AI (GPT-2 קטן)
generator = pipeline("text-generation", model="gpt2")

# בחירת רובוט
selected_robot = st.selectbox("בחר רובוט לשלוח לו הודעה:", list(robots.keys()))

# הצגת תמונת הרובוט
robot_image = Image.open(robots[selected_robot])
st.image(robot_image, width=200)

# הזנת הודעה
message = st.text_input("כתוב את ההודעה שלך לרובוט:")

# פונקציה ליצירת תגובת רובוט חכמה
def robot_response_ai(msg):
    prompt = f"הודעה לרובוט: '{msg}'. תגובת הרובוט:"
    response = generator(prompt, max_length=50, num_return_sequences=1)
    return response[0]['generated_text'].split("תגובת הרובוט:")[-1].strip()

# שליחת הודעה
if st.button("שלח הודעה"):
    if message.strip() != "":
        if "history" not in st.session_state:
            st.session_state.history = []
        # הוספת הודעת המשתמש
        st.session_state.history.append(f"אתה -> {selected_robot}: {message}")
        # תגובת הרובוט
        response = robot_response_ai(message)
        st.session_state.history.append(f"{selected_robot} -> אתה: {response}")
    else:
        st.error("נא להקליד הודעה לפני השליחה!")

# הצגת היסטוריית הודעות
if "history" in st.session_state and st.session_state.history:
    st.subheader("📜 היסטוריית הודעות")
    for msg in st.session_state.history:
        st.write(msg)
