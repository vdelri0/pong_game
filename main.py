"""_summary_

steps:

- 1. Create the screen
- 2. Create and move the paddle
- 3. Create another paddle
- 4. Create the ball and make it move
- 5. Detect collision with wall and bounce
- 6. Detect collision with paddle
- 7. Detect when paddle misses ball
- 8. Keep score

"""
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from random import choice

import time

ON = True
SPEED = 1
SLEEP = 0.07 # How fast the ball is going to move
WIDTH = 800
HEIGHT = 600

class Main():
    def __init__(
        self,
        color,
        title,
        scoreboard: Scoreboard,
        l_paddle: Paddle,
        r_paddle: Paddle,
        ball: Ball
    ):

        # Create the screen
        self.screen = Screen()
        self.screen.bgcolor(color)
        self.screen.title(title)
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.tracer(0) #Turn off the animation

        # Assign the scoreboard, paddle and ball
        self.scoreboard = scoreboard
        self.l_paddle = l_paddle
        self.r_paddle = r_paddle
        self.ball = ball

        # Set keybindings
        self.screen.listen()
        self.screen.onkey(self.r_paddle.up, "Up")
        self.screen.onkey(self.r_paddle.down, "Down")

        self.screen.onkey(self.l_paddle.up, "w")
        self.screen.onkey(self.l_paddle.down, "s")

    def play(self):
        while ON:
            time.sleep(SLEEP)
            self.screen.update()
            self.ball.move()

            self.collide_with_wall()
            self.collide_with_paddle()
        self.screen.exitonclick()

    def collide_with_wall(self):
        # Detect collision with wall
        if self.ball.xcor() == 390:
            self.scoreboard.increase_score("left")
            self.reset_ball()
        elif self.ball.xcor() == -390:
            self.scoreboard.increase_score("right")
            self.reset_ball()

        self.check_score()

        if self.ball.ycor() >= 290 or self.ball.ycor() <= -290:
            self.ball.bounce_y()

    def collide_with_paddle(self):
        # Detect collision with paddle
        if self.ball.distance(self.l_paddle) < 20 and ball.xcor() <= -370:
            self.ball.bounce_x()

        if self.ball.distance(self.r_paddle) < 20 and ball.xcor() >= 370:
            self.ball.bounce_x()

    def check_score(self):
        if self.scoreboard.get_left_score() == 10 or self.scoreboard.get_right_score() == 10:
            self.game_over()

    def reset_ball(self):
        self.ball.goto(0,0)
        self.ball.bounce_x()
        self.ball.bounce_y()

    def game_over(self):
        global ON
        ON = False
        self.scoreboard.game_over()

if __name__ == "__main__":
    # Create the scoreboard, paddles and ball
    paddles = []
    ball = Ball()
    scoreboard = Scoreboard()
    l_paddle = Paddle(position=(-385, 0), len=0.5, wid=2)
    r_paddle = Paddle(position=(380, 0), len=0.5, wid=2)

    # Run game
    color = "black"
    title = "Ping Pong Game"
    main = Main(color, title, scoreboard, l_paddle, r_paddle, ball)
    main.play()
