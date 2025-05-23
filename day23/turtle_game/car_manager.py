from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.i = 0
        if 6 - self.i <= 2 :
            self.i = 2
        

    def create_car(self):
        random_chance = random.randint(1, 6 - self.i)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1,stretch_len=2) 
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level(self):
        self.car_speed += MOVE_INCREMENT
        if 6 - self.i <= 2 :
            self.i = 2
        else:
            self.i += 1

        

