from turtle import Turtle, Screen
import random

tt = Turtle()
sc = Screen()

colors = ["royal blue","midnight blue","saddle brown","crimson","dark red","green yellow","lime","olive drab","violet"]
directions = [0, 90, 180, 270]
tt.pensize(15)


for _ in range(200):
    tt.color(random.choice(colors))
    tt.right(random.choice(directions))
    tt.forward(30)



sc.exitonclick()

    
    