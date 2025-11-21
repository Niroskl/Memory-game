import streamlit as st
import random

st.set_page_config(page_title="🤖 רובוטים חכמים + מוזיקה מתקדמת", layout="wide")
st.title("🤖 רובוטים חכמים + מוזיקה 🎵")

# רובוטים עם תמונות מהאינטרנט
robots = {
    "רובוט דובר": "https://via.placeholder.com/200?text=רובוט+דובר",
    "רובוט מנקה": "https://via.placeholder.com/200?text=רובוט+מנקה",
    "רובוט שמירה": "https://via.placeholder.com/200?text=רובוט+שמירה",
    "רובוט עוזר": "https://via.placeholder.com/200?text=רובוט+עוזר"
}

# שירים שונים לפי רובוט
robot_songs = {
    "רובוט דובר": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "רובוט מנקה": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "רובוט שמירה": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    "רובוט עוזר": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
}

# יצירת היסטוריה אם לא קיימת
if "history" not in st.session_state:
    st.session_state.history = []

# מילון לשמירת תגובות שכבר נאמרו לכל רובוט
if "used_responses" not in st.session_state:
    st.session_state.used_responses = {}

# בחירת רובוט
selected_robot = st.selectbox("בחר רובוט לשלוח לו הודעה:", list(robots.keys()))

# הצגת תמונת הרובוט
st.image(robots[selected_robot], width=200)

# פונקציה שמחזירה תגובה אקראית לפי מילות מפתח
def robot_response(msg, robot_name):
    msg = msg.lower()
    
    if "גנב" in msg or "סכנה" in msg:
        responses = ["אני שולח את השמירה מיד!", "אני מתריע למערכת הביטחון!", "השמירה בדרך!"]
    elif "עזרה" in msg:
        responses = ["אני בדרך, הישאר רגוע!", "אני מגיע לעזרתך!", "אל דאגה, אני כאן!"]
    elif "טוב" in msg or "בסדר" in msg:
        responses = ["מצוין, אני ממשיך במעקב.", "כל בסדר, ממשיך לפעול.", "הכל מתנהל כרגיל."]
    elif "חבר" in msg or "אחי" in msg:
        responses = ["חחח אחי, אני תמיד כאן בשבילך!", "תודה אחי, שמח להיות חבר שלך!", "חבר טוב צריך תמיד להקשיב!"]
    else:
        responses = ["מעניין, ספר לי עוד!", "סיפור מעניין, אני מקשיב.", "ספר לי עוד פרטים!"]

    # שמירה על חזרתיות נמוכה
    if robot_name not in st.session_state.used_responses:
        st.session_state.used_responses[robot_name] = []

    available_responses = [r for r in responses if r not in st.session_state.used_responses[robot_name]]
    
    if not available_responses:
        st.session_state.used_responses[robot_name] = []
        available_responses = responses

    chosen = random.choice(available_responses)
    st.session_state.used_responses[robot_name].append(chosen)
    return chosen

# שימוש ב-form
with st.form(key="message_form"):
    message = st.text_input("כתוב את ההודעה שלך לרובוט:")
    submit_button = st.form_submit_button(label="שלח הודעה")
    
    if submit_button:
        if message.strip() != "":
            # הוספת הודעת המשתמש והתגובה של הרובוט
            st.session_state.history.append(f"אתה -> {selected_robot}: {message}")
            response = robot_response(message, selecte_
