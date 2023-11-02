from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.sety(280)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, "center", ("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, "center", ("Courier", 30, "normal"))

