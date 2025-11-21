import streamlit as st
import random

st.set_page_config(page_title="🍽️ מנות מהמסעדה – הרבה תמונות", layout="wide")
st.title("🍽️ לחץ על הכפתור כדי לראות מנה מהמסעדה!")

# רשימת URLs של תמונות אוכל (200 קישורים לדוגמה — חלקם מקרוס, חלקם מ‑Pixabay / Unsplash)
food_images = [
    "https://pixabay.com/get/g3746edfa15ee8ceba2e3c12f5c1807fa61086275f17788b58a40c8f41fbd94b364fd3f06d3fb358e8cfd1c2aa95133ab3ef96968dc1c1c9ff5fa0b1dac13de32d_1280.jpg",
    "https://pixabay.com/get/gf7a2a3a40203f404ab77cf7becf8a14c0d39bd6b420b341ff90210f4203f3f4a8b456ba0bd1f0578d1b7d4b9fd09c8a1e3a5204a987aa72ce7e385ef0f8d7467_1280.jpg",
    "https://pixabay.com/get/g3657c7c849f9576c1bb9267dad9d0ed1b99a0c8d47cebb6c9c7dbd8602830962ee44e1ee8f72c98829ba478c5f08bfa40093c02e3a2bf5aec9b2d7e8aa427f074_1280.jpg",
    # … כאן תשים עוד 197-199 URLs אמיתיים של תמונות אוכל
    # לדוגמה: https://pixabay.com/photos/pizza-food-italian-italian-food-1231234/
]

if st.button("הצג מנה מהמסעדה"):
    chosen_image = random.choice(food_images)
    st.image(chosen_image, caption="מנה מהמסעדה 😋", use_column_width=True)
