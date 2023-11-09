from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.color("blue")


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    current_loop = 0
    while current_loop < side:
        turtle.forward(100)
        turtle.left(angle)
        current_loop += 1


def change_pen_color():
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor(r, g, b)


for side in range(3, 11):
    change_pen_color()
    draw_shape(side)
    side += 1

screen = Screen()
screen.exitonclick()
