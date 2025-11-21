import streamlit as st
import random
import time

st.set_page_config(page_title="משחק מחני אוכל משודרג", layout="wide")

# אתחול
if "table" not in st.session_state:
    st.session_state.table = []
if "score" not in st.session_state:
    st.session_state.score = 0

st.title("🍽️ משחק מחני אוכל - גרסה משודרגת 🍽️")
st.write("סמן כמה מוצרים ולחץ כדי להניח אותם על השולחן בבת אחת!")

# רשימת מוצרים מורחבת
foods = ["🍎", "🍌", "🍔", "🍕", "🍣", "🍪", "🥗", "🌭", 
         "🥖", "🍩", "🍇", "🍉", "🥥", "🥛", "🧋", "🍫", "🍿", "🍟", "🥪", "🥓"]

# בחירה מרובה
selected_foods = st.multiselect("בחר את המוצרים להנחה על השולחן:", foods)

# כפתור להנחה
if st.button("🍽️ מחן את כולם עכשיו!"):
    if selected_foods:
        st.session_state.table.extend(selected_foods)
        st.session_state.score += len(selected_foods)
        st.balloons()  # קונפטי
        # צליל
        st.markdown("""
            <audio autoplay>
                <source src="pour.mp3" type="audio/mp3">
            </audio>
        """, unsafe_allow_html=True)
    else:
        st.warning("❗ בחר לפחות מוצר אחד")

# שולחן גרפי עם מיקום רנדומלי לכל מוצר
st.subheader("השולחן שלך:")
st.markdown('<div style="position:relative; width:100%; height:500px; background: linear-gradient(135deg, #ffe5d9, #ffd6a5, #fdffb6, #caffbf); border-radius:20px;">', unsafe_allow_html=True)
for item in st.session_state.table:
    top = random.randint(10, 400)
    left = random.randint(10, 900)
    rotation = random.randint(-30, 30)
    st.markdown(f'''
        <div style="position:absolute; top:{top}px; left:{left}px; font-size:50px; transform: rotate({rotation}deg);">
            {item}
        </div>
    ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.write(f"🥇 נקודות: {st.session_state.score}")
