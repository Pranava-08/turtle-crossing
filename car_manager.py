COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_ZONE = (-240, 240)
from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.cars = []
        self.n = 6

    def new_car(self):
        k = random.randint(1,self.n)
        if k == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(400 ,random.randint(-240, 240) )
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            self.cars.append(new_car)

    def move_cars(self, x):
        for car in self.cars:
            if car.xcor()>-450:
                car.forward(x)