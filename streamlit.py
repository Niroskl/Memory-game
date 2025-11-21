# התקנת הספרייה
!pip install pywhatkit

import pywhatkit as kit

# שליחת הודעה
phone_number = "+972501234567"  # מספר יעד כולל קידומת מדינה
message = "שלום! זו הודעה שנשלחה דרך Python 😊"
hour = 12   # שעה
minute = 30 # דקות

# שליחה ל‑WhatsApp Web (יפתח את הדפדפן אוטומטית)
kit.sendwhatmsg(phone_number, message, hour, minute)
