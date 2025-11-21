import streamlit as st
import random

st.set_page_config(page_title="💅 משחק עיצוב ציפורניים משודרג", layout="wide")
st.title("💅 עיצוב ציפורניים – עכשיו עם עוד אביזרים!")

colors = ["לבן", "ורוד", "אדום", "כחול", "שחור", "זהב", "כסף", "סגול", "ירוק", "כתום"]
patterns = ["חלקה", "פסים", "נקודות", "זיגזג", "לב", "כוכב", "נוצות", "גליטר", "Ombre"]
accessories = [
    "ללא", "פנירה", "קישוט לב", "קישוט כוכב", "נצנץ", "דבק נוצות",
    "אבני חן", "סרטים דקורטיביים", "פרח קטן", "קונפטי צבעוני"
]

num_nails = 10
nails = {}

st.write("בחרי צבע, דוגמה ואביזר לכל ציפורן:")

for i in range(1, num_nails+1):
    st.subheader(f"ציפורן {i}")
    color = st.selectbox(f"בחרי צבע לציפורן {i}", colors, key=f"color{i}")
    pattern = st.selectbox(f"בחרי דוגמה לציפורן {i}", patterns, key=f"pattern{i}")
    accessory = st.selectbox(f"בחרי אביזר לציפורן {i}", accessories, key=f"acc{i}")
    nails[f"ציפורן {i}"] = (color, pattern, accessory)

# כפתור להצגת עיצוב סופי
if st.button("הצג את הציפורניים שלך"):
    st.write("💅 עיצוב סופי של הציפורניים שלך:")
    for nail, (color, pattern, acc) in nails.items():
        st.write(f"{nail}: צבע {color}, דוגמה {pattern}, אביזר: {acc}")

# כפתור עיצוב רנדומלי
if st.button("צור עיצוב אוטומטי"):
    st.write("💅 עיצוב אוטומטי:")
    for i in range(1, num_nails+1):
        color = random.choice(colors)
        pattern = random.choice(patterns)
        acc = random.choice(accessories)
        st.write(f"ציפורן {i}: צבע {color}, דוגמה {pattern}, אביזר: {acc}")
