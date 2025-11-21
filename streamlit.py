# רשימת רובים
guns = ["רובה AK", "רובה M4", "רובה Sniper", "רובה Shotgun"]

# פונקציה לשלוח הודעה / פעולה לרובה
def send_message(gun, message):
    print(f"שלחנו ל-{gun}: {message}")

# משחק - המשתמש בוחר רובה ומקליד הודעה
while True:
    print("\nרובים זמינים:")
    for i, gun in enumerate(guns, 1):
        print(f"{i}. {gun}")
    
    choice = input("בחר מספר רובה לשלוח לו הודעה (או 'q' ליציאה): ")
    
    if choice.lower() == 'q':
        print("סיימנו את המשחק!")
        break
    
    if choice.isdigit() and 1 <= int(choice) <= len(guns):
        gun = guns[int(choice) - 1]
        message = input("כתוב את ההודעה שלך לרובה: ")
        send_message(gun, message)
    else:
        print("בחירה לא חוקית. נסה שוב.")
