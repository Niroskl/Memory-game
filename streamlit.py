import streamlit as st
import random
import time

st.set_page_config(page_title="Memory Game", layout="wide")

# --- COLORFUL BACKGROUND ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
        }
        @keyframes gradientBG {
            0%{background-position:0% 50%}
            50%{background-position:100% 50%}
            100%{background-position:0% 50%}
        }
        .big-card button {
            font-size: 40px !important;
            padding: 30px !important;
            height: 120px !important;
            width: 120px !important;
            border-radius: 15px !important;
        }
    </style>
""", unsafe_allow_html=True)


# --- SHAPES ---
SHAPES = ["🔵", "🔺", "⭐", "❤️", "⚫", "⬛", "🌙", "🟧",
          "🟢", "🔶", "🟣", "❄️", "🍀", "🔥", "💎", "⚡"]


# --- INITIALIZATION ---
if "cards" not in st.session_state:
    values = SHAPES * 2
    random.shuffle(values)

    st.session_state.cards = values
    st.session_state.revealed = [False] * 32
    st.session_state.temp_reveal = [False] * 32
    st.session_state.first_pick = None
    st.session_state.matches = 0
    st.session_state.start_time = time.time()
    st.session_state.block = False

    # PLAYER SYSTEM
    st.session_state.current_player = 1
    st.session_state.score = {1: 0, 2: 0}


# --- GAME LOGIC FUNCTIONS ---
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
        st.session_state.revealed[first] = True
        st.session_state.revealed[second] = True
        st.session_state.matches += 1

        # Player scores a point
        st.session_state.score[st.session_state.current_player] += 1

        st.session_state.temp_reveal[first] = False
        st.session_state.temp_reveal[second] = False

    else:
        # Wait & hide
        st.session_state.block = True
        st.session_state.hide_time = time.time() + 1

        # Switch player
        st.session_state.current_player = 2 if st.session_state.current_player == 1 else 1

    st.session_state.first_pick = None


def process_hiding():
    if st.session_state.block and time.time() > st.session_state.hide_time:
        st.session_state.temp_reveal = [False] * 32
        st.session_state.block = False


process_hiding()

# --- DISPLAY ---
st.title("🎨 Memory Game — Two Players Edition")

elapsed = int(time.time() - st.session_state.start_time)
st.write(f"⏱️ זמן: **{elapsed} שניות**")

colA, colB = st.columns(2)

with colA:
    st.subheader("👤 Player 1")
    st.write(f"ניקוד: **{st.session_state.score[1]}**")

with colB:
    st.subheader("👤 Player 2")
    st.write(f"ניקוד: **{st.session_state.score[2]}**")

st.write(f"🎯 עכשיו משחק: **Player {st.session_state.current_player}**")

cols = st.columns(8)

for i in range(32):
    col = cols[i % 8]

    with col:
        if st.session_state.revealed[i] or st.session_state.temp_reveal[i]:
            st.button(st.session_state.cards[i], key=f"card{i}", disabled=True)
        else:
            st.markdown('<div class="big-card">', unsafe_allow_html=True)
            st.button("❓", key=f"card{i}", on_click=pick_card, args=(i,))
            st.markdown('</div>', unsafe_allow_html=True)

# Winner message
if sum(st.session_state.revealed) == 32:
    if st.session_state.score[1] > st.session_state.score[2]:
        st.success("🏆 Player 1 ניצח!")
    elif st.session_state.score[2] > st.session_state.score[1]:
        st.success("🏆 Player 2 ניצח!")
    else:
        st.info("🤝 תיקו!")
