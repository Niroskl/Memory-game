import streamlit as st
import pywhatkit as kit
from datetime import datetime

st.title("📱 WhatsApp Messenger - Streamlit App")

# הזנת מספר טלפון
phone_number = st.text_input("הכנס מספר טלפון (כולל קידומת מדינה, לדוגמה +972501234567)")

# הזנת הודעה
message = st.text_area("כתוב את ההודעה שלך כאן")

# בחירת שליחה מיידית או לפי שעה
send_type = st.radio("בחר סוג שליחה:", ("מיידית", "לפי שעה"))

if st.button("שלח הודעה"):
    if not phone_number or not message:
        st.error("אנא מלא את כל השדות")
    else:
        if send_type == "מיידית":
            try:
                kit.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=True)
                st.success("✅ ההודעה נשלחה בהצלחה!")
            except Exception as e:
                st.error(f"שגיאה בשליחה: {e}")
        else:
            now = datetime.now()
            hour = st.number_input("שעה לשליחה (0-23):", min_value=0, max_value=23, value=now.hour)
            minute = st.number_input("דקה לשליחה (0-59):", min_value=0, max_value=59, value=now.minute+1)
            try:
                kit.sendwhatmsg(phone_number, message, hour, minute)
                st.success(f"✅ ההודעה נקבעה לשליחה ב-{hour}:{minute}")
            except Exception as e:
                st.error(f"שגיאה בתזמון ההודעה: {e}")
