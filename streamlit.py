import streamlit as st
from PIL import Image

st.set_page_config(page_title="🤖 רובוטים חכמים בלי AI", layout="wide")
st.title("🤖 רובוטים חכמים - Streamlit (ללא AI)")

# רובוטים עם תמונה
robots = {
    "רובוט דובר": "robot_speaker.png",
    "רובוט מנקה": "robot_cleaner.png",
    "רובוט שמירה": "robot_guard.png",
    "רובוט עוזר": "robot_helper.png"
}

# בחירת רובוט
selected_robot = st.selectbox("בחר רובוט לשלוח לו הודעה:", list(robots.keys()))

# הצגת תמונת הרובוט
robot_image = Image.open(robots[selected_robot])
st.image(robot_image, width=200)

# הזנת הודעה
message = st.text_input("כתוב את ההודעה שלך לרובוט:")

# פונקציה שמחזירה תגובה לפי מילות מפתח
def robot_response(msg):
    msg = msg.lower()
    if "גנב" in msg or "סכנה" in msg:
        return "אני שולח את השמירה מיד!"
    elif "עזרה" in msg:
        return "אני בדרך, הישאר רגוע!"
    elif "טוב" in msg or "בסדר" in msg:
        return "מצוין, אני ממשיך במעקב."
    else:
        return "מעניין, ספר לי עוד!"

# כפתור לשליחת הודעה
if st.button("שלח הודעה"):
    if message.strip() != "":
        if "history" not in st.session_state:
            st.session_state.history = []
        # הוספת הודעת המשתמש
        st.session_state.history.append(f"אתה -> {selected_robot}: {message}")
        # תגובת הרובוט לפי לוגיקה
        response = robot_response(message)
        st.session_state.history.append(f"{selected_robot} -> אתה: {response}")
    else:
        st.error("נא להקליד הודעה לפני השליחה!")

# הצגת היסטוריה של הודעות
if "history" in st.session_state and st.session_state.history:
    st.subheader("📜 היסטוריית הודעות")
    for msg in st.session_state.history:
        st.write(msg)
