import streamlit as st
import random

st.set_page_config(page_title="🍽️ מנה של מסעדה", layout="wide")
st.title("🍽️ לחץ על הכפתור כדי לראות את המנה של המסעדה!")

# רשימת תמונות של מנות מהמסעדה (אפשר להכניס קבצים מקומיים או URL)
food_images = [
    "restaurant_food1.jpg",  # קובץ מקומי
    "restaurant_food2.jpg",  # קובץ מקומי
    "https://example.com/restaurant_food3.jpg",  # URL
    "https://example.com/restaurant_food4.jpg"   # URL
]

# כפתור שמציג תמונה רנדומלית של מנה
if st.button("הצג את המנה של המסעדה"):
    chosen_image = random.choice(food_images)
    st.image(chosen_image, caption="מנה מהמסעדה 😋", use_column_width=True)
