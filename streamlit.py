import streamlit as st
import random

st.title("🍽️ לחץ על הכפתור כדי לראות מנה מהמסעדה!")

# URLs ישירים של תמונות אוכל
food_images = [
    "https://cdn.pixabay.com/photo/2017/05/07/08/56/pizza-2291087_1280.jpg",
    "https://cdn.pixabay.com/photo/2016/03/05/19/02/hamburger-1238246_1280.jpg",
    "https://cdn.pixabay.com/photo/2015/04/08/13/13/food-712665_1280.jpg",
    "https://cdn.pixabay.com/photo/2017/06/02/18/24/salad-2362241_1280.jpg",
    "https://cdn.pixabay.com/photo/2014/10/19/20/59/hamburger-494706_1280.jpg"
]

if st.button("הצג מנה מהמסעדה"):
    chosen_image = random.choice(food_images)
    st.image(chosen_image, caption="מנה מהמסעדה 😋", use_column_width=True)
