from turtle import Turtle, Screen
import random

tartaruga = Turtle()
screen = Screen()

colors = ["royal blue","midnight blue","saddle brown","crimson","dark red","green yellow","lime","olive drab","violet"]

def draw_shape(num_sides):
    angle = 360 / num_sides 
    for _ in range(num_sides):   
        tartaruga.right(angle)
        tartaruga.forward(100)
    
for shape_side_n in range(3,11):
    tartaruga.color(random.choice(colors))
    draw_shape(shape_side_n)



screen.exitonclick()