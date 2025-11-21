import streamlit as st
import random

st.set_page_config(page_title="🤖 רובוטים חכמים בלי AI", layout="wide")
st.title("🤖 רובוטים חכמים - Streamlit (ללא AI)")

# רובוטים עם תמונות מהאינטרנט
robots = {
    "רובוט דובר": "https://via.placeholder.com/200?text=רובוט+דובר",
    "רובוט מנקה": "https://via.placeholder.com/200?text=רובוט+מנקה",
    "רובוט שמירה": "https://via.placeholder.com/200?text=רובוט+שמירה",
    "רובוט עוזר": "https://via.placeholder.com/200?text=רובוט+עוזר"
}

# יצירת היסטוריה אם לא קיימת
if "history" not in st.session_state:
    st.session_state.history = []

# יצירת מילון לשמירת תגובות שכבר נאמרו לכל רובוט
if "used_responses" not in st.session_state:
    st.session_state.used_responses = {}

# בחירת רובוט
selected_robot = st.selectbox("בחר רובוט לשלוח לו הודעה:", list(robots.keys()))

# הצגת תמונת הרובוט ישירות מה-URL
st.image(robots[selected_robot], width=200)

# פונקציה שמחזירה תגובה אקראית לפי מילות מפתח, בלי חזרות
def robot_response(msg, robot_name):
    msg = msg.lower()
    
    if "גנב" in msg or "סכנה" in msg:
        responses = ["אני שולח את השמירה מיד!", "אני מתריע למערכת הביטחון!", "השמירה בדרך!"]
    elif "עזרה" in msg:
        responses = ["אני בדרך, הישאר רגוע!", "אני מגיע לעזרתך!", "אל דאגה, אני כאן!"]
    elif "טוב" in msg or "בסדר" in msg:
        responses = ["מצוין, אני ממשיך במעקב.", "כל בסדר, ממשיך לפעול.", "הכל מתנהל כרגיל."]
    else:
        responses = ["מעניין, ספר לי עוד!", "סיפור מעניין, אני מקשיב.", "ספר לי עוד פרטים!"]

    # יצירת רשימת תגובות שכבר נאמרו עבור הרובוט
    if robot_name not in st.session_state.used_responses:
        st.session_state.used_responses[robot_name] = []

    # רשימת תגובות זמינות שלא נאמרו עדיין
    available_responses = [r for r in responses if r not in st.session_state.used_responses[robot_name]]
    
    if not available_responses:
        # אם כל התגובות נאמרו, לאפס ולהתחיל מחדש
        st.session_state.used_responses[robot_name] = []
        available_responses = responses

    chosen = random.choice(available_responses)
    st.session_state.used_responses[robot_name].append(chosen)
    return chosen

# שימוש ב-form כדי שהשדה לא ייעלם
with st.form(key="message_form"):
    message = st.text_input("כתוב את ההודעה שלך לרובוט:")
    submit_button = st.form_submit_button(label="שלח הודעה")
    
    if submit_button:
        if message.strip() != "":
            # הוספת הודעת המשתמש והתגובה האקראית של הרובוט
            st.session_state.history.append(f"אתה -> {selected_robot}: {message}")
            st.session_state.history.append(f"{selected_robot} -> אתה: {robot_response(message, selected_robot)}")
        else:
            st.error("נא להקליד הודעה לפני השליחה!")

# הצגת היסטוריה של הודעות
st.subheader("📜 היסטוריית הודעות")
for msg in st.session_state.history:
    st.write(msg)
