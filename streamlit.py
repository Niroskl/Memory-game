import streamlit as st
import time

st.set_page_config(page_title="משחק שוקו", layout="wide")

# אתחול
if "score" not in st.session_state:
    st.session_state.score = 0

st.title("🍫 משחק השוקו שלך 🍫")
st.write("מזוג שוקו לכוס כמה שיותר מהר!")

# כפתור מזיגת שוקו
if st.button("🫖 מזוג שוקו!"):
    st.session_state.score += 1
    st.balloons()  # קונפטי
    st.markdown("""
        <audio autoplay>
            <source src="pour.mp3" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)

st.write(f"🥛 כוסות שוקו שמילאת: {st.session_state.score}")

# אפשרות טיימר
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

elapsed = int(time.time() - st.session_state.start_time)
st.write(f"⏱ זמן שעבר: {elapsed} שניות")
