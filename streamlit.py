import streamlit as st
from datetime import datetime
import calendar

# =======================
# עיצוב עמוד: רקע טורקיז וטקסט לבן
st.markdown(
    """
    <style>
    body {
        background-color: #40E0D0;  /* טורקיז */
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #008080;  /* ירוק-טורקיז כהה */
        color: white;
        font-size: 18px;
        padding: 8px;
        border-radius: 5px;
    }
    .stButton>button {
        background-color: #006666;
        color: white;
        font-size: 18px;
        padding: 8px 16px;
        border-radius: 5px;
    }
    .calendar {
        width: 100%;
        max-width: 500px;
        border-collapse: collapse;
        margin-top: 20px;
    }
    .calendar th, .calendar td {
        border: 1px solid white;
        text-align: center;
        padding: 10px;
    }
    .calendar th {
        background-color: #006666;
    }
    .calendar td {
        background-color: #008080;
        font-size: 18px;
    }
    .today {
        background-color: #FFD700 !important;  /* צהוב לזהות היום */
        color: black;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="📅 יום ומזל אסטרולוגי", layout="centered")
st.title("📅 איזה יום זה + מזל אסטרולוגי")

# =======================
# פונקציה למזל אסטרולוגי מדויק
def zodiac_sign(day, month):
    zodiac = [
        ("גדי", (22,12),(19,1), "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Capricorn_symbol.svg/120px-Capricorn_symbol.svg.png"),
        ("דלי", (20,1),(18,2), "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Aquarius_symbol.svg/120px-Aquarius_symbol.svg.png"),
        ("דגים", (19,2),(20,3), "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Pisces_symbol.svg/120px-Pisces_symbol.svg.png"),
        ("טלה", (21,3),(19,4), "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Aries_symbol.svg/120px-Aries_symbol.svg.png"),
        ("שור", (20,4),(20,5), "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Taurus_symbol.svg/120px-Taurus_symbol.svg.png"),
        ("תאומים", (21,5),(20,6), "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Gemini_symbol.svg/120px-Gemini_symbol.svg.png"),
        ("סרטן", (21,6),(22,7), "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cancer_symbol.svg/120px-Cancer_symbol.svg.png"),
        ("אריה", (23,7),(22,8), "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Leo_symbol.svg/120px-Leo_symbol.svg.png"),
        ("בתולה", (23,8),(22,9), "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Virgo_symbol.svg/120px-Virgo_symbol.svg.png"),
        ("מאזניים", (23,9),(22,10), "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Libra_symbol.svg/120px-Libra_symbol.svg.png"),
        ("עקרב", (23,10),(21,11), "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Scorpio_symbol.svg/120px-Scorpio_symbol.svg.png"),
        ("קשת", (22,11),(21,12), "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Sagittarius_symbol.svg/120px-Sagittarius_symbol.svg.png")
    ]
    
    for sign, start, end, img in zodiac:
        start_day, start_month = start
        end_day, end_month = end
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sign, img
    return None, None

# =======================
# קלט תאריך
date_input = st.text_input("הכנס תאריך (DD/MM/YYYY)", "")

if date_input:
    try:
        user_date = datetime.strptime(date_input, "%d/%m/%Y")
        day_index = user_date.weekday()  # Monday=0 ... Sunday=6
        days_hebrew = ["יום שני", "יום שלישי", "יום רביעי", "יום חמישי", "יום שישי", "שבת", "יום ראשון"]
        day_hebrew = days_hebrew[day_index]
        
        st.success(f"התאריך {date_input} הוא: **{day_hebrew}**")

        # =======================
        # הצגת לוח שנה גרפי מסודר
        st.subheader("📆 לוח השנה החודשי")
        cal = calendar.monthcalendar(user_date.year, user_date.month)

        # HTML table עם סדר ימי השבוע: א׳ ב׳ ג׳ ד׳ ה׳ ו׳ שבת
        table_html = "<table class='calendar'><tr>"
        weekdays_hebrew = ["א'", "ב'", "ג'", "ד'", "ה'", "ו'", "שבת"]
        for day_name in weekdays_hebrew:
            table_html += f"<th>{day_name}</th>"
        table_html += "</tr>"

        for week in cal:
            table_html += "<tr>"
            # התאמת סדר לפי א׳ עד שבת
            ordered_week = [week[6]] + week[:6]  # שבוע מתחיל עם ראשון (index 6), ואז שני-שישי
            for day in ordered_week:
                if day == 0:
                    table_html += "<td></td>"
                elif day == user_date.day:
                    table_html += f"<td class='today'>{day}</td>"
                else:
                    table_html += f"<td>{day}</td>"
            table_html += "</tr>"
        table_html += "</table>"

        st.markdown(table_html, unsafe_allow_html=True)

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
