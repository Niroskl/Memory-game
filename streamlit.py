import streamlit as st
import random
import time

st.set_page_config(page_title="Memory Game", layout="wide")


# ------------------ יפה: רקע מעוצב וצבעוני ------------------
st.markdown("""
    <style>
        body {
            background: linear-gradient(120deg, #ff9a9e, #fecfef, #a1c4fd, #c2e9fb);
            background-size: 300% 300%;
            animation: beautifulBG 12s ease infinite;
        }

        @keyframes beautifulBG {
            0%   {background-position: 0% 50%;}
            50%  {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        /* הכרטיסים הענקיים */
        .big-card button {
            font-size: 80px !important;
            height: 220px !important;
            width: 220px !important;
            padding: 40px !important;
            border-radius: 25px !important;
            background-color: white !important;
            box-shadow: 0px 0px 12px rgba(0,0,0,0.4);
        }
    </style>
""", unsafe_allow_html=True)


# ------------------ סמלים ------------------
SHAPES = ["🔵", "🔺", "⭐", "❤️", "⚫", "⬛", "🌙", "🟧",
          "🟢", "🔶", "🟣", "❄️", "🍀", "🔥", "💎", "⚡"]


# ------------------ אתחול המשחק ------------------
if "cards" not in st.session_state:
    values = SHAPES * 2
    random.shuffle(values)

    st.session_state.cards = values
    st.session_state.revealed = [False] * 32
    st.session_state.temp_reveal = [False] * 32
    st.session_state.first_pick = None
    st.session_state.block = False
    st.session_state.hide_time = None

    # שני שחקנים בעברית
    st.session_state.current_player = 1
    st.session_state.score = {1: 0, 2: 0}


# ------------------ לוגיקה ------------------
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
        # התאמה!
        st.session_state.revealed[first] = True
        st.session_state.revealed[second] = True

        # ניקוד
        st.session_state.score[st.session_state.current_player] += 1

        # אפקט קונפטי 🎉
        st.balloons()

        # צליל נעים 🎵
        try:
            audio_file = open("match.mp3", "rb")
            st.audio(audio_file.read(), format="audio/mp3")
        except:
            pass

        # לא מסתירים כי זו התאמה
        st.session_state.temp_reveal[first] = False
        st.session_state.temp_reveal[second] = False

    else:
        # לא התאמה → מסתיר אחרי שנייה
        st.session_state.block = True
        st.session_state.hide_time = time.time() + 1

        # החלפת תור בין שחקנים
        st.session_state.current_player = 2 if st.session_state.current_player == 1 else 1

    st.session_state.first_pick = None


def process_hiding():
    if st.session_state.block and time.time() > st.session_state.hide_time:
        st.session_state.temp_reveal = [False] * 32
        st.session_state.block = False


process_hiding()


# ------------------ תצוגה ------------------
st.title("🎨 משחק הזיכרון — גרסת היוקרה")

colA, colB = st.columns(2)

with colA:
    st.subheader("👤 שחקן 1")
    st.write(f"ניקוד: **{st.session_state.score[1]}**")

with colB:
    st.subheader("👤 שחקן 2")
    st.write(f"ניקוד: **{st.session_state.score[2]}**")

st.write(f"🎯 התור של: **שחקן {st.session_state.current_player}**")

cols = st.columns(4)  # 4 בעמודה כדי להתאים לכרטיסים הגדולים

for i in range(32):
    with cols[i % 4]:
        st.markdown('<div class="big-card">', unsafe_allow_html=True)
        if st.session_state.revealed[i] or st.session_state.temp_reveal[i]:
            st.button(st.session_state.cards[i], key=f"c{i}", disabled=True)
        else:
            st.button("❓", key=f"c{i}", on_click=pick_card, args=(i,))
        st.markdown('</div>', unsafe_allow_html=True)


# ------------------ סיום משחק ------------------
if all(st.session_state.revealed):
    if st.session_state.score[1] > st.session_state.score[2]:
        st.success("🏆 שחקן 1 ניצח!")
    elif st.session_state.score[2] > st.session_state.score[1]:
        st.success("🏆 שחקן 2 ניצח!")
    else:
        st.info("🤝 תיקו!")
