import streamlit as st
import random

st.title("🤖 משחק רובוטים פעילים - Streamlit")

# רשימת רובוטים
robots = ["רובוט דובר", "רובוט מנקה", "רובוט שמירה", "רובוט עוזר"]

# תגובות אפשריות של הרובוטים
responses = [
    "הבנתי אותך!",
    "אני עובד על זה…",
    "זה מעניין!",
    "מצוין!",
    "תמשיך כך!"
]

# בחירת רובוט
selected_robot = st.selectbox("בחר רובוט לשלוח לו הודעה:", robots)

# הזנת הודעה
message = st.text_input("כתוב את ההודעה שלך לרובוט:")

# כפתור לשליחה
if st.button("שלח הודעה"):
    if message.strip() != "":
        if "history" not in st.session_state:
            st.session_state.history = []
        # הוספת הודעת המשתמש
        st.session_state.history.append(f"אתה -> {selected_robot}: {message}")
        # הוספת תגובת הרובוט
        bot_response = random.choice(responses)
        st.session_state.history.append(f"{selected_robot} -> אתה: {bot_response}")
    else:
        st.error("נא להקליד הודעה לפני השליחה!")

# הצגת היסטוריית הודעות
if "history" in st.session_state and st.session_state.history:
    st.subheader("📜 היסטוריית הודעות")
    for msg in st.session_state.history:
        st.write(msg)
