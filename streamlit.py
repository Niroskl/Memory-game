import streamlit as st
import random

st.set_page_config(page_title="🍽️ מה יש לאכול במסדה?", layout="wide")
st.title("🍽️ מה יש לאכול במסדה? 🍽️")
st.write("לחץ על הכפתור והמחשב יציג תמונה של אוכל של מסדה!")

# רשימת תמונות של אוכל (קבצים מקומיים או URL)
food_images = [
    "masada_food1.jpg",
    "masada_food2.jpg",
    "masada_food3.jpg",
    "masada_food4.jpg"
]

# כפתור להצגת תמונה רנדומלית
if st.button("גלה מה יש לאכול!"):
    chosen_image = random.choice(food_images)
    st.image(chosen_image, caption="האוכל של מסדה 😋", use_column_width=True)
