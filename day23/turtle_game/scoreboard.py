from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "left"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update()

    def update(self):
        self.goto(-280,260)
        self.write(f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)


    def point(self):
        self.level += 1
        self.clear()
        self.update()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)