from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.penup()
        self.color("white")
        self.write_score()

    def get_left_score(self):
        return self.left_score

    def get_right_score(self):
        return self.right_score

    def write_score(self):
        self.goto(0, 260)
        self.write(f"{self.left_score} - {self.right_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self, left_or_right):
        if left_or_right == "left":
            self.left_score += 1
        else:
            self.right_score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
