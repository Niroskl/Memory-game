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

# יצירת היסטוריה ושדה קלט אם לא קיימים
if "history" not in st.session_state:
    st.session_state.history = []

if "current_message" not in st.session_state:
    st.session_state.current_message = ""

# בחירת רובוט
selected_robot = st.selectbox("בחר רובוט לשלוח לו הודעה:", list(robots.keys()))

# הצגת תמונת הרובוט
robot_image = Image.open(robots[selected_robot])
st.image(robot_image, width=200)

# הזנת הודעה ושמירה ב-session_state
st.session_state.current_message = st.text_input("כתוב את ההודעה שלך לרובוט:", st.session_state.current_message)

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

# כפתור לשליחה
if st.button("שלח הודעה"):
    message = st.session_state.current_message.strip()
    if message != "":
        # שמירת הודעה בהיסטוריה
        st.session_state.history.append(f"אתה -> {selected_robot}: {message}")
        st.session_state.history.append(f"{selected_robot} -> אתה: {robot_response(message)}")
        st.session_state.current_message = ""  # מנקה את השדה אחרי שליחה
    else:
        st.error("נא להקליד הודעה לפני השליחה!")

# הצגת היסטוריה
st.subheader("📜 היסטוריית הודעות")
for msg in st.session_state.history:
    st.write(msg)
