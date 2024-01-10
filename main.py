import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')

game_onn = True
i = 0
t = 0.1 # screen sleep time
d = 7 # car move distance
level = 1
while game_onn:
    time.sleep(t)
    screen.update()
    scoreboard.score(level)
    cars.new_car()
    cars.move_cars(d)
    for car in cars.cars:
        if player.distance(car) < 20:
            game_onn = False
            scoreboard.game_over()
    if player.ycor() > 270:
        player.reset()
        i += 1
        level += 1
        d+=5
        t*0.7
        if i %2 == 0:
            if cars.n > 2:
                cars.n -= 1
        
    


screen.exitonclick()