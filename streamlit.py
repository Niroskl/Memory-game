import streamlit as st
import random

# --- הגדרת דף ---
st.set_page_config(page_title="🍽️ מנות מהמסעדה", layout="wide")
st.title("🍽️ לחץ על הכפתור כדי לראות מנה מהמסעדה!")

# --- רשימת 50 תמונות של מנות מהאינטרנט ---
food_images = [
    "https://images.unsplash.com/photo-1600891964599-f61ba0e24092?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1551782450-a2132b4ba21d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1525755662778-989d0524087e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1617196030351-c8d8e4f4f4c3?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1562967916-eb82221dfb47?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1600891964599-3c8f2d3f7eae?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1617196030444-d8e1f0b5a8e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    # ... הוסף כאן את שאר 40 התמונות לפי הצורך
]

# --- כפתור שמציג תמונה רנדומלית ---
if st.button("הצג מנה מהמסעדה"):
    chosen_image = random.choice(food_images)
    st.image(chosen_image, caption="מנה מהמסעדה 😋", use_column_width=True)
