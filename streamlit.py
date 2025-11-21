import streamlit as st
import random
import time

st.set_page_config(page_title="Memory Game", layout="wide")

# --- OPTIONAL MUSIC ---
# כדי להפעיל מוזיקה ברקע, העלה קובץ mp3 לאפליקציה והפעל את השורה הבאה:
# st.audio("music.mp3", autoplay=True)

# --- CSS for Bigger Cards ---
st.markdown("""
    <style>
        .big-card button {
            font-size: 80px !important;
            padding: 60px !important;
            height: 240px !important;
            width: 240px !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- SHAPES ---
SHAPES = ["🔵", "🔺", "⭐", "❤️", "⚫", "⬛", "🌙", "🟧",
          "🟢", "🔶", "🟣", "❄️", "🍀", "🔥", "💎", "⚡"]

# --- INITIALIZATION ---
if "cards" not in st.session_state:
    values = SHAPES * 2  # 16 pairs → 32 cards
    random.shuffle(values)

    st.session_state.cards = values
    st.session_state.revealed = [False] * 32
    st.session_state.temp_reveal = [False] * 32
    st.session_state.first_pick = None
    st.session_state.matches = 0
    st.session_state.start_time = time.time()
    st.session_state.block = False


# --- FUNCTIONS ---
def pick_card(index):
    if st.session_state.block:
        return
    if st.session_state.revealed[index] or st.session_state.temp_reveal[index]:
        return

    st.session_state.temp_reveal[index] = True

    if st.session_state.first_pick is None:
        st.session_state.first_pick = index
        return

    first = st.session_state.first_pick
    second = index

    if st.session_state.cards[first] == st.session_state.cards[second]:
        # match
        st.session_state.revealed[first] = True
        st.session_state.revealed[second] = True
        st.session_state.matches += 1
        st.session_state.temp_reveal[first] = False
        st.session_state.temp_reveal[second] = False
    else:
        # mismatch → show briefly
        st.session_state.block = True
        st.session_state.hide_time = time.time() + 0.9

    st.session_state.first_pick = None


def process_hiding():
    if st.session_state.block and time.time() > st.session_state.hide_time:
        st.session_state.temp_reveal = [False] * 32
        st.session_state.block = False


# --- GAME LOGIC ---
process_hiding()

st.title("🎨 Memory Game — Shapes Edition")

elapsed = int(time.time() - st.session_state.start_time)
st.write(f"⏱️ זמן: **{elapsed} שניות**")
st.write(f"🎯 זוגות שמצאת: **{st.session_state.matches} / 16**")

cols = st.columns(8)

for i in range(32):
    col = cols[i % 8]

    with col:
        if st.session_state.revealed[i] or st.session_state.temp_reveal[i]:
            st.button(st.session_state.cards[i], key=f"card{i}", disabled=True, help="", kwargs=None, type="secondary")
        else:
            st.markdown('<div class="big-card">', unsafe_allow_html=True)
            st.button("❓", key=f"card{i}", on_click=pick_card, args=(i,))
            st.markdown('</div>', unsafe_allow_html=True)

# win message
if st.session_state.matches == 16:
    st.success("🎉 ניצחת! מצאת את כל הזוגות!")
