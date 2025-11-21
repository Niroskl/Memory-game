from vpython import *

# יצירת סצנה
scene = canvas(title="🏎️ סימולציית מכונית 3D", width=800, height=600)

# יצירת מסלול
track = box(pos=vector(0,0,0), size=vector(20,0.5,5), color=color.gray(0.5))

# יצירת מכונית (קוביה פשוטה)
car = box(pos=vector(-8,0.5,0), size=vector(2,1,1), color=color.red)

# פונקציה להזזת המכונית קדימה
def move_car():
    for i in range(50):
        rate(10)  # מהירות התנועה
        car.pos.x += 0.3

# התחלת התנועה
move_car()
