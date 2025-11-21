import streamlit as st

st.title("🤖 רובוטים שמבינים קצת - Streamlit")

robots = ["רובוט דובר", "רובוט מנקה", "רובוט שמירה", "רובוט עוזר"]

selected_robot = st.selectbox("בחר רובוט לשלוח לו הודעה:", robots)
message = st.text_input("כתוב את ההודעה שלך לרובוט:")

# פונקציה שמחזירה תגובה לפי מילות מפתח
def robot_response(msg):
    msg = msg.lower()
    if "גנב" in msg or "סכנה" in msg:
        return "אני שולח את השמירה מיד!"
    elif "טוב" in msg or "בסדר" in msg:
        return "מצוין, אני ממשיך במעקב."
    elif "עזרה" in msg:
        return "אני בדרך, הישאר רגוע!"
    else:
        return "מעניין, ספר לי עוד!"

if st.button("שלח הודעה"):
    if message.strip() != "":
        if "history" not in st.session_state:
            st.session_state.history = []
        st.session_state.history.append(f"אתה -> {selected_robot}: {message}")
        st.session_state.history.append(f"{selected_robot} -> אתה: {robot_response(message)}")
    else:
        st.error("נא להקליד הודעה לפני השליחה!")

# הצגת היסטוריה
if "history" in st.session_state and st.session_state.history:
    st.subheader("📜 היסטוריית הודעות")
    for msg in st.session_state.history:
        st.write(msg)
