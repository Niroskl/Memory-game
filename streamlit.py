import streamlit as st
import random

st.set_page_config(page_title="משחק מחני אוכל - יחד", layout="wide")

# אתחול
if "table" not in st.session_state:
    st.session_state.table = []  # רשימת המוצרים שכבר מונחו
if "score" not in st.session_state:
    st.session_state.score = 0

st.title("🍽️ משחק מחני אוכל - מחנים כמה מוצרים בבת אחת 🍽️")
st.write("סמן כמה מוצרים ולחץ על הכפתור כדי להניח את כולם על השולחן בבת אחת!")

# רשימת מוצרים
foods = ["🍎", "🍌", "🍔", "🍕", "🍣", "🍪", "🥗", "🌭", "🥖", "🍩"]

# בחירה מרובה
selected_foods = st.multiselect("בחר את המוצרים:", foods)

# כפתור להנחה
if st.button("🍽️ מחן את כולם עכשיו!"):
    if selected_foods:
        # הוסף את כולם לשולחן
        st.session_state.table.extend(selected_foods)
        st.session_state.score += len(selected_foods)
        # קונפטי
        st.balloons()
        # צליל
        st.markdown("""
            <audio autoplay>
                <source src="pour.mp3" type="audio/mp3">
            </audio>
        """, unsafe_allow_html=True)
    else:
        st.warning("❗ בחר לפחות מוצר אחד")

# הצגת השולחן - מיקום רנדומלי לכל מוצר
st.subheader("השולחן שלך:")
st.markdown('<div style="position:relative; width:100%; height:400px; background-color:#fff8dc; border-radius:15px;">', unsafe_allow_html=True)
for item in st.session_state.table:
    top = random.randint(10, 350)
    left = random.randint(10, 800)
    st.markdown(f'''
        <div style="position:absolute; top:{top}px; left:{left}px; font-size:50px;">
            {item}
        </div>
    ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.write(f"🥇 נקודות: {st.session_state.score}")
