import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

#Declaracao de Classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#Movimento do Player
screen.listen()
screen.onkey(player.go_foward,"w")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > 285:
        scoreboard.point()
        player.update()
        car_manager.level()
    
    for car in car_manager.all_cars :
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False




screen.exitonclick()