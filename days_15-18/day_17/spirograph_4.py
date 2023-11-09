from turtle import Turtle, Screen
import random


def change_pen_color():
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor(r, g, b)


turtle = Turtle()
turtle.speed(0)
for circle_number in range(100):
    change_pen_color()
    turtle.circle(100)
    turtle.left(360 / 100)

screen = Screen()
screen.exitonclick()
