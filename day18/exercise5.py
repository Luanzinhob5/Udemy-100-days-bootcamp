import turtle as t
import random

tim = t.Turtle()
sc = t.Screen()
t.colormode(255)

tim.speed(1000)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tupla = (r,g,b)
    return tupla

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

sc.exitonclick()