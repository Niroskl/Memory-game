import streamlit as st

st.title("🎵 נגני מוזיקה עם בחירה מראש")

songs = {
    "שיר 1": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "שיר 2": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "שיר 3": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"
}

# כפתורים לבחירת שיר
for name, url in songs.items():
    if st.button(f"הפעל {name}"):
        st.audio(url, format="audio/mp3")
