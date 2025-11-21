import streamlit as st
import random
import time

st.set_page_config(page_title="Memory Game", layout="wide")

# סמלים
SHAPES = ["🔵", "🔺", "⭐", "❤️", "⚫", "⬛", "🌙", "🟧",
          "🟢", "🔶", "🟣", "❄️", "🍀", "🔥", "💎", "⚡"]

# אתחול
if "cards" not in st.session_state:
    values = SHAPES * 2
    random.shuffle(values)
    st.session_state.cards = values
    st.session_state.revealed = [False]*32
    st.session_state.first_pick = None
    st.session_state.block = False
    st.session_state.hide_time = None
    st.session_state.current_player = 1
    st.session_state.score = {1:0,2:0}
    # סיבוב אקראי לכל קלף (-15° עד 15°)
    st.session_state.rotation = [random.randint(-15, 15) for _ in range(32)]

def pick_card(i):
    if st.session_state.block or st.session_state.revealed[i]:
        return

    if st.session_state.first_pick is None:
        st.session_state.first_pick = i
        return
    else:
        first = st.session_state.first_pick
        second = i
        if st.session_state.cards[first] == st.session_state.cards[second]:
            st.session_state.revealed[first] = True
            st.session_state.revealed[second] = True
            st.session_state.score[st.current_player] += 1
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
        st.session_state.block = False

process_hiding()

# CSS
st.markdown("""
<style>
body {background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);}
.card-button button {
    font-size:80px !important;
    width:280px !important;
    height:280px !important;
    margin:8px !important;
    border-radius:20px !important;
    background-color:white !important;
    box-shadow:0 0 15px rgba(0,0,0,0.4);
    display:flex;
    justify-content:center;
    align-items:center;
}
.player-score {font-size:20px; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# שחקנים
st.title("🎨 משחק הזיכרון — קלפים גדולים ומסובבים")
col1,col2 = st.columns(2)
with col1:
    st.subheader("👤 שחקן 1")
    st.markdown(f"<div class='player-score'>ניקוד: {st.session_state.score[1]}</div>", unsafe_allow_html=True)
with col2:
    st.subheader("👤 שחקן 2")
    st.markdown(f"<div class='player-score'>ניקוד: {st.session_state.score[2]}</div>", unsafe_allow_html=True)

st.write(f"🎯 התור של: **שחקן {st.session_state.current_player}**")

# המשחק
st.markdown('<div style="display:flex; flex-wrap:wrap; justify-content:center;">', unsafe_allow_html=True)
for i in range(32):
    label = st.session_state.cards[i] if st.session_state.revealed[i] or st.session_state.first_pick==i else "❓"
    rotation = st.session_state.rotation[i]
    st.markdown(f'''
        <div class="card-button" style="transform: rotate({rotation}deg);">
            <button onclick="return false">{label}</button>
        </div>
    ''', unsafe_allow_html=True)
    if not st.session_state.revealed[i] and not st.session_state.first_pick==i:
        st.button("", key=f"btn{i}", on_click=pick_card, args=(i,), help="לחץ לחשוף")
st.markdown('</div>', unsafe_allow_html=True)

# סיום משחק
if all(st.session_state.revealed):
    if st.session_state.score[1] > st.session_state.score[2]:
        st.success("🏆 שחקן 1 ניצח!")
    elif st.session_state.score[2] > st.session_state.score[1]:
        st.success("🏆 שחקן 2 ניצח!")
    else:
        st.info("🤝 תיקו!")
