import cv2
import time

# טוען את המודל לזיהוי גוף מלא
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

cap = cv2.VideoCapture(0)  # מצלמה

score = 0
detected_last_frame = []  # רשימה לשמירת אנשים שנמצאו בפריים הקודם
cooldown = 1.0  # שניות בין זיהוי אדם חדש
last_detect_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_cascade.detectMultiScale(gray, 1.1, 3)

    current_time = time.time()
    new_detection = False

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

        # אם עבר מספיק זמן מאז הזיהוי האחרון, נספור נקודה
        if current_time - last_detect_time > cooldown:
            score += 1
            last_detect_time = current_time
            new_detection = True

        # אפקט מהפנט: עיגול צבעוני מעל האדם
        cv2.circle(frame, (x + w//2, y), 20, (255, 0, 255), -1)

    cv2.putText(frame, f"Score: {score}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Hypnotize People Game', frame)

    # יציאה בלחיצה על 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
