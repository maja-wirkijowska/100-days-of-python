from turtle import Turtle, Screen
import random


def change_pen_color():
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor(r, g, b)


def select_direction():
    directions = [0, 90, 180, 270]
    random_direction = random.choice(directions)
    return random_direction


turtle = Turtle()
turtle.shape("turtle")
turtle.color("blue")
turtle.pensize(10)
turtle.speed(8)

for _ in range(200):
    change_pen_color()
    turtle.forward(25)
    turtle.setheading(select_direction())

screen = Screen()
screen.exitonclick()
