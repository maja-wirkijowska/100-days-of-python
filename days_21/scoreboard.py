from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))

    def left_point(self):
        self.left_score += 1
        self.clear()
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.clear()
        self.update_score()
