import streamlit as st
from datetime import datetime
import calendar

# =======================
# הגדרות עיצוב - רקע שחור וצבע טקסט לבן
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #222222;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="📅 איזה יום זה?", layout="centered")
st.title("📅 בדיקת יום בשבוע + מזל אסטרולוגי")

# =======================
# פונקציה לקביעת מזל לפי יום וחודש
def zodiac_sign(day, month):
    zodiac = [
        ("דגים", 20, 3, 19, 4, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Aries_symbol.svg/120px-Aries_symbol.svg.png"),
        ("טלה", 20, 4, 20, 5, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Aries_symbol.svg/120px-Aries_symbol.svg.png"),
        ("שור", 21, 5, 20, 6, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Taurus_symbol.svg/120px-Taurus_symbol.svg.png"),
        ("תאומים", 21, 6, 22, 7, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Gemini_symbol.svg/120px-Gemini_symbol.svg.png"),
        ("סרטן", 23, 7, 22, 8, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cancer_symbol.svg/120px-Cancer_symbol.svg.png"),
        ("אריה", 23, 8, 22, 9, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Leo_symbol.svg/120px-Leo_symbol.svg.png"),
        ("בתולה", 23, 9, 22, 10, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Virgo_symbol.svg/120px-Virgo_symbol.svg.png"),
        ("מאזניים", 23, 10, 21, 11, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Libra_symbol.svg/120px-Libra_symbol.svg.png"),
        ("עקרב", 22, 11, 21, 12, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Scorpio_symbol.svg/120px-Scorpio_symbol.svg.png"),
        ("קשת", 22, 12, 19, 1, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Sagittarius_symbol.svg/120px-Sagittarius_symbol.svg.png"),
        ("גדי", 20, 1, 18, 2, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Capricorn_symbol.svg/120px-Capricorn_symbol.svg.png"),
        ("דגים", 19, 2, 19, 3, "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Pisces_symbol.svg/120px-Pisces_symbol.svg.png")
    ]
    
    for sign, start_day, start_month, end_day, end_month, img in zodiac:
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sign, img
    return None, None

# =======================
# קלט מהמשתמש
date_input = st.text_input("הכנס תאריך (DD/MM/YYYY)", "")

if date_input:
    try:
        user_date = datetime.strptime(date_input, "%d/%m/%Y")
        day_index = user_date.weekday()  # Monday=0 ... Sunday=6
        days_hebrew = ["יום שני", "יום שלישי", "יום רביעי", "יום חמישי", "יום שישי", "שבת", "יום ראשון"]
        day_hebrew = days_hebrew[day_index]

        st.success(f"התאריך {date_input} הוא: **{day_hebrew}**")

        # =======================
        # הצגת לוח שנה חודשי
        st.subheader("📆 לוח שנה של החודש")
        cal = calendar.month(user_date.year, user_date.month)
        st.text(cal)

        # =======================
        # הצגת מזל אסטרולוגי
        sign, img_url = zodiac_sign(user_date.day, user_date.month)
        if sign:
            st.subheader(f"♈️ המזל האסטרולוגי שלך הוא: {sign}")
            st.image(img_url, width=120)
        else:
            st.write("לא הצלחנו לקבוע את המזל.")

    except ValueError:
        st.error("פורמט התאריך לא נכון! השתמש ב-DD/MM/YYYY")
