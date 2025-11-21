import streamlit as st
from datetime import datetime

st.set_page_config(page_title="📅 איזה יום זה?", layout="centered")
st.title("📅 בדיקת יום בשבוע")

st.write("כתוב תאריך בפורמט: **YYYY-MM-DD** (שנה-חודש-יום) כדי לדעת איזה יום בשבוע זה.")

# קלט מהמשתמש
date_input = st.text_input("הכנס תאריך (לדוגמה: 2025-11-21)")

if date_input:
    try:
        # המרה לתאריך
        user_date = datetime.strptime(date_input, "%Y-%m-%d")
        # קבלת שם היום בעברית
        days_hebrew = ["יום שני", "יום שלישי", "יום רביעי", "יום חמישי", "יום שישי", "שבת", "יום ראשון"]
        day_index = user_date.weekday()  # Monday=0 ... Sunday=6
        # תיקון אינדקס לשמות בעברית
        day_hebrew = days_hebrew[day_index]
        
        # תצוגה
        st.success(f"התאריך {date_input} הוא: **{day_hebrew}**")
    except ValueError:
        st.error("פורמט התאריך לא נכון! השתמש בפורמט YYYY-MM-DD.")
