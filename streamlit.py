from vpython import *

scene = canvas(title="🏎️ משחק מכוניות 3D", width=800, height=600)

# מסלול
track = box(pos=vector(0,0,0), size=vector(20,0.5,5), color=color.gray(0.5))

# מכונית
car = box(pos=vector(-8,0.5,0), size=vector(2,1,1), color=color.red)

# פונקציה לשליטה
def move_car(evt):
    if evt.key == "up":
        car.pos.x += 0.5
    elif evt.key == "left":
        car.pos.z -= 0.5
    elif evt.key == "right":
        car.pos.z += 0.5
    elif evt.key == "down":
        car.pos.x -= 0.5

scene.bind("keydown", move_car)
