from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self, speed="fastest", len=0.5, wid=0.5):
        # Create the ball
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed(speed)
        self.shapesize(stretch_len=len, stretch_wid=wid)
        self.penup()

        # Define the x,y modifiers for movement
        self.move_x = 10
        self.move_y = 10

    def get_move_x(self):
        return self.move_x

    def set_move_x(self, move_x):
        self.move_x = move_x

    def get_move_y(self):
        return self.move_y

    def set_move_y(self, move_y):
        self.move_y = move_y

    def move(self):
        # Move the ball
        xcor = self.xcor() + self.move_x
        ycor = self.ycor() + self.move_y
        self.goto(xcor, ycor)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
