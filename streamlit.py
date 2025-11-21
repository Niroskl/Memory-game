import streamlit as st

st.title("🏎️ סימולציה: נסיעה עם מכונית")

# הגדרת מיקום ההתחלתי
if "x" not in st.session_state:
    st.session_state.x = 0
    st.session_state.y = 0

# פקודות לנהיגה
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ שמאלה"):
        st.session_state.x -= 1
with col2:
    if st.button("⬆️ קדימה"):
        st.session_state.y += 1
with col3:
    if st.button("➡️ ימינה"):
        st.session_state.x += 1

# הצגת המיקום הנוכחי
st.write(f"🚗 מיקום המכונית: X = {st.session_state.x}, Y = {st.session_state.y}")

# אפשר להוסיף מסלול גרפי עם emojis או תמונות:
track = [["⬜"]*10 for _ in range(10)]
# סימון המכונית במיקום הנוכחי
x = max(0, min(st.session_state.x, 9))
y = max(0, min(st.session_state.y, 9))
track[y][x] = "🚗"

# הצגת המסלול
for row in track[::-1]:  # הופכים את המסלול כדי Y=0 למטה
    st.write(" ".join(row))
