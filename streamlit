import streamlit as st
import random
import time

st.set_page_config(page_title="Memory Game", layout="wide")

# --- INITIALIZATION ---
if "cards" not in st.session_state:
    values = list(range(1, 17)) * 2  # 32 cards (16 pairs)
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

    # Flip the card
    st.session_state.temp_reveal[index] = True

    # If first pick
    if st.session_state.first_pick is None:
        st.session_state.first_pick = index
        return

    # Second pick
    first = st.session_state.first_pick
    second = index

    if st.session_state.cards[first] == st.session_state.cards[second]:
        # Match
        st.session_state.revealed[first] = True
        st.session_state.revealed[second] = True
        st.session_state.matches += 1
        st.session_state.temp_reveal[first] = False
        st.session_state.temp_reveal[second] = False
    else:
        # Not a match → briefly show, then hide on next rerun
        st.session_state.block = True

        # Schedule hiding
        st.session_state.hide_time = time.time() + 0.8

    st.session_state.first_pick = None


def process_hiding():
    if st.session_state.block and time.time() > st.session_state.hide_time:
        st.session_state.temp_reveal = [False] * 32
        st.session_state.block = False


# --- GAME LOGIC ---
process_hiding()

st.title("🃏 Memory Game – 32 Cards")

elapsed = int(time.time() - st.session_state.start_time)
st.write(f"⏱️ Time: **{elapsed} seconds**")
st.write(f"🎯 Matches: **{st.session_state.matches} / 16**")

cols = st.columns(8)

for i in range(32):
    col = cols[i % 8]

    with col:
        if st.session_state.revealed[i] or st.session_state.temp_reveal[i]:
            st.button(f"{st.session_state.cards[i]}", key=f"card{i}", disabled=True)
        else:
            if st.button("❓", key=f"card{i}", on_click=pick_card, args=(i,)):
                pass

# Win message
if st.session_state.matches == 16:
    st.success("🎉 כל הכבוד! מצאת את כל הזוגות!")
