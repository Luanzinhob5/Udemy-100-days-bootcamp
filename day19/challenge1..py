from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def move_right():
    tim.right(15)

def move_left():
    tim.left(15)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
    
screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(move_right,"d")
screen.onkey(move_left,"a")
screen.onkey(clear_screen,"c")
screen.exitonclick()