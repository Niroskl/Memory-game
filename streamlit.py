import streamlit as st
import random

st.set_page_config(page_title="🍽️ מנות מהמסעדה", layout="wide")
st.title("🍽️ לחץ על הכפתור כדי לראות מנה מהמסעדה!")

# רשימת תמונות (30 מנות שונות מהאינטרנט)
food_images = [
    "https://images.unsplash.com/photo-1600891964599-f61ba0e24092",  # פיצה
    "https://images.unsplash.com/photo-1551782450-a2132b4ba21d",      # המבורגר
    "https://images.unsplash.com/photo-1546069901-ba9599a7e63c",      # סושי
    "https://images.unsplash.com/photo-1525755662778-989d0524087e",  # סלט
    "https://images.unsplash.com/photo-1617196030351-c8d8e4f4f4c3",  # עוגה
    "https://images.unsplash.com/photo-1562967916-eb82221dfb47",      # פסטה
    "https://images.unsplash.com/photo-1627308595229-7830a5c91f9f",  # סנדוויץ'
    "https://images.unsplash.com/photo-1600891964599-3c8f2d3f7eae",  # דונאט
    "https://images.unsplash.com/photo-1504674900247-0877df9cc836",  # שייק
    "https://images.unsplash.com/photo-1617196030444-d8e1f0b5a8e2",  # מרק
    "https://images.unsplash.com/photo-1543332164-3812e43b0713",      # טוסט
    "https://images.unsplash.com/photo-1600891964887-9e05d3f8e64c",  # נקניקיה
    "https://images.unsplash.com/photo-1598514982793-cd084b6c51f6",  # פנקייק
    "https://images.unsplash.com/photo-1598514982704-7f0f4d39fbbc",  # כריך
    "https://images.unsplash.com/photo-1586190848861-99aa4a171e90",  # סושי מגש
    "https://images.unsplash.com/photo-1562967914-2e2f37fef230",      # סלט ירוק
    "https://images.unsplash.com/photo-1617196030333-6c8d1d0e1a6b",  # עוגת שוקולד
    "https://images.unsplash.com/photo-1600891964600-7e7cbe1f3f2e",  # פיצה מרגריטה
    "https://images.unsplash.com/photo-1551782451-aaa4b4b6b38f",      # המבורגר עם גבינה
    "https://images.unsplash.com/photo-1546069902-72d0d7e6f3f9",      # סלט פירות
    "https://images.unsplash.com/photo-1600891964589-2a2f2e0e0a2b",  # דונאט צבעוני
    "https://images.unsplash.com/photo-1562967915-8c0f0e0d0f0b",      # שייק פירות
    "https://images.unsplash.com/photo-1617196030445-5c8b1d0d3b7c",  # מרק ירקות
    "https://images.unsplash.com/photo-1598514982800-8d0f1b1c2d3e",  # פנקייק עם סירופ
    "https://images.unsplash.com/photo-1600891964590-4b2f2c0e1a3f",  # סושי רול
    "https://images.unsplash.com/photo-1543332163-1b2e3c4d5e6f",      # עוגת גבינה
    "https://images.unsplash.com/photo-1562967916-3f4e5d6c7b8a",      # פסטה עם רוטב
    "https://images.unsplash.com/photo-1617196030334-2b8d1f0a3c7d",  # סנדוויץ' גבינה
    "https://images.unsplash.com/photo-1600891964588-3c1f2e0d1a4b",  # נקניקיה עם לחם
    "https://images.unsplash.com/photo-1598514982794-2d0e3f4c5b6a"   # טוסט עם ירקות
]

# כפתור שמציג תמונה רנדומלית
if st.button("הצג מנה מהמסעדה"):
    chosen_image = random.choice(food_images)
    st.image(chosen_image, caption="מנה מהמסעדה 😋", use_column_width=True)
