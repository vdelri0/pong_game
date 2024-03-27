from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position, len, wid, speed="fastest"):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_len=len, stretch_wid=wid)
        self.speed("fastest")
        self.penup()
        self.goto(position)

    def up(self):
        xcor = self.xcor()
        ycor = self.ycor() + 10
        self.goto(xcor, ycor)

    def down(self):
        xcor = self.xcor()
        ycor = self.ycor() - 10
        self.goto(xcor, ycor)