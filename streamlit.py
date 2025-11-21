from vpython import *

# יצירת סצנה
scene = canvas(title="🏎️ משחק מכוניות 3D", width=800, height=600, center=vector(0,0,0))

# מסלול
track = box(pos=vector(0,0,0), size=vector(40,0.5,10), color=color.gray(0.5))

# מכונית
car = box(pos=vector(-18,0.5,0), size=vector(2,1,1), color=color.red)

# פונקציה לשליטה במכונית
def move_car(evt):
    if evt.key == "up":
        car.pos.x += 0.5
    elif evt.key == "down":
        car.pos.x -= 0.5
    elif evt.key == "left":
        car.pos.z -= 0.5
    elif evt.key == "right":
        car.pos.z += 0.5

scene.bind("keydown", move_car)

# לולאה פשוטה לשמירה על סצנה פעילה
while True:
    rate(60)
