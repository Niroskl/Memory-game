import streamlit as st
import random
import time

st.set_page_config(page_title="Memory Game", layout="wide")

SHAPES = ["🔵", "🔺", "⭐", "❤️", "⚫", "⬛", "🌙", "🟧",
          "🟢", "🔶", "🟣", "❄️", "🍀", "🔥", "💎", "⚡"]

if "cards" not in st.session_state:
    values = SHAPES * 2
    random.shuffle(values)

    st.session_state.cards = values
    st.session_state.revealed = [False] * 32
    st.session_state.temp_reveal = [False] * 32
    st.session_state.first_pick = None
    st.session_state.block = False
    st.session_state.hide_time = None
    st.session_state.current_player = 1
    st.session_state.score = {1: 0, 2: 0}

def pick_card(i):
    if st.session_state.block:
        return
    if st.session_state.revealed[i] or st.session_state.temp_reveal[i]:
        return

    st.session_state.temp_reveal[i] = True

    if st.session_state.first_pick is None:
        st.session_state.first_pick = i
        return

    first = st.session_state.first_pick
    second = i

    if st.session_state.cards[first] == st.session_state.cards[second]:
        st.session_state.revealed[first] = True
        st.session_state.revealed[second] = True
        st.session_state.score[st.session_state.current_player] += 1
        st.session_state.temp_reveal[first] = False
        st.session_state.temp_reveal[second] = False
        st.balloons()
        st.markdown("""
            <audio autoplay>
                <source src="match.mp3" type="audio/mp3">
            </audio>
        """, unsafe_allow_html=True)
    else:
        st.session_state.block = True
        st.session_state.hide_time = time.time() + 1
        st.session_state.current_player = 2 if st.session_state.current_player == 1 else 1

    st.session_state.first_pick = None

def process_hiding():
    if st.session_state.block and time.time() > st.session_state.hide_time:
        st.session_state.temp_reveal = [False] * 32
        st.session_state.block = False

process_hiding()

# CSS חדש עם כרטיסים גדולים באמת
st.markdown("""
<style>
.game-container {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
    padding: 20px;
    border-radius: 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
.card {
    font-size: 80px !important;
    width: 220px !important;
    height: 220px !important;
    margin: 10px;
    border-radius: 25px !important;
    background-color: white !important;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.4);
}
.player-score {
    font-size: 24px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# שחקנים בעברית
st.title("🎨 משחק הזיכרון — גרסת היוקרה")
colA, colB = st.columns(2)
with colA:
    st.subheader("👤 שחקן 1")
    st.markdown(f"<div class='player-score'>ניקוד: {st.session_state.score[1]}</div>", unsafe_allow_html=True)
with colB:
    st.subheader("👤 שחקן 2")
    st.markdown(f"<div class='player-score'>ניקוד: {st.session_state.score[2]}</div>", unsafe_allow_html=True)

st.write(f"🎯 התור של: **שחקן {st.session_state.current_player}**")

# המשחק עצמו עם פריסה גמישה
st.markdown('<div class="game-container">', unsafe_allow_html=True)

for i in range(32):
    card_html = f'<div class="card">{st.session_state.cards[i] if (st.session_state.revealed[i] or st.session_state.temp_reveal[i]) else "❓"}</div>'
    st.markdown(card_html, unsafe_allow_html=True)
    if not st.session_state.revealed[i] and not st.session_state.temp_reveal[i]:
        if st.button("", key=f"btn{i}", on_click=pick_card, args=(i,), help="לחץ כדי לחשוף"):
            pass

st.markdown('</div>', unsafe_allow_html=True)

# סיום משחק
if all(st.session_state.revealed):
    if st.session_state.score[1] > st.session_state.score[2]:
        st.success("🏆 שחקן 1 ניצח!")
    elif st.session_state.score[2] > st.session_state.score[1]:
        st.success("🏆 שחקן 2 ניצח!")
    else:
        st.info("🤝 תיקו!")
