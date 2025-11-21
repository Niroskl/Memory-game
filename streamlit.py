import streamlit as st
from transformers import pipeline

st.title("🤖 רובוטים עם AI - Streamlit")

# יצירת pipeline של Text Generation
generator = pipeline("text-generation", model="gpt2")  # מודל קטן

robots = ["רובוט דובר", "רובוט מנקה", "רובוט שמירה", "רובוט עוזר"]

selected_robot = st.selectbox("בחר רובוט לשלוח לו הודעה:", robots)
message = st.text_input("כתוב את ההודעה שלך לרובוט:")

# פונקציה ליצירת תגובת רובוט חכמה
def robot_response_ai(msg):
    prompt = f"הודעה לרובוט: '{msg}'. תגובת הרובוט:"
    response = generator(prompt, max_length=50, num_return_sequences=1)
    return response[0]['generated_text'].split("תגובת הרובוט:")[-1].strip()

if st.button("שלח הודעה"):
    if message.strip() != "":
        if "history" not in st.session_state:
            st.session_state.history = []
        st.session_state.history.append(f"אתה -> {selected_robot}: {message}")
        response = robot_response_ai(message)
        st.session_state.history.append(f"{selected_robot} -> אתה: {response}")
    else:
        st.error("נא להקליד הודעה לפני השליחה!")

# הצגת היסטוריה
if "history" in st.session_state and st.session_state.history:
    st.subheader("📜 היסטוריית הודעות")
    for msg in st.session_state.history:
        st.write(msg)
