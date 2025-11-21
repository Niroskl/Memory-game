import streamlit as st

st.title("🎵 נגני מוזיקה אוטומטית")

# URL של קובץ MP3
url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

# נגינה
st.audio(url, format="audio/mp3")
