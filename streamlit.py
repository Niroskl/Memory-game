import streamlit as st

st.title("🤖 שליחת הודעות לרובוטים - Streamlit Game")

# רשימת רובוטים
robots = ["רובוט דובר", "רובוט מנקה", "רובוט שמירה", "רובוט עוזר"]

# בחירת רובוט
selected_robot = st.selectbox("בחר רובוט לשלוח לו הודעה:", robots)

# הזנת הודעה
message = st.text_input("כתוב את ההודעה שלך לרובוט:")

# כפתור לשליחה
if st.button("שלח הודעה"):
    if message.strip() != "":
        st.success(f"שלחנו ל-{selected_robot}: {message}")
        # שמירה בהיסטוריה
        if "history" not in st.session_state:
            st.session_state.history = []
        st.session_state.history.append(f"{selected_robot}: {message}")
    else:
        st.error("נא להקליד הודעה לפני השליחה!")

# הצגת היסטוריית הודעות
if "history" in st.session_state and st.session_state.history:
    st.subheader("📜 היסטוריית הודעות")
    for msg in st.session_state.history:
        st.write(msg)
