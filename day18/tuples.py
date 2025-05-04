import turtle as t
import random

tt = t.Turtle()
sc = t.Screen()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tupla = (r,g,b)
    return tupla

directions = [0, 90, 180, 270]
tt.pensize(15)


for _ in range(200):
    tt.color(random_color())
    tt.right(random.choice(directions))
    tt.forward(30)



sc.exitonclick()