from turtle import Turtle, Screen

end = True
a = 0
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
        




screen = Screen()
screen.exitonclick()