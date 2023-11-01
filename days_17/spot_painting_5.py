from turtle import Turtle, Screen
import random


def generate_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


colors = []
up = 50
for _ in range(10):
    colors.append(generate_random_color())
turtle = Turtle()
turtle.speed(0)
turtle.penup()
turtle.goto(-200, -200)
num_of_dots = 100
for dot_count in range(1, num_of_dots + 1):
    turtle.pendown()
    turtle.dot(25, random.choice(colors))
    turtle.penup()
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)  # turn to face up
        turtle.forward(50)  # move up
        turtle.setheading(180)  # turn to face left
        turtle.forward(500)  # move all the way left
        turtle.setheading(0)  # face right


screen = Screen()
screen.exitonclick()
