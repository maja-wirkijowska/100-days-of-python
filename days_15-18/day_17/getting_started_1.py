from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("blue")

for _ in range(4):
    turtle.forward(100.0)
    turtle.right(90)

turtle.penup()
turtle.goto(0, 30)

for _ in range(15):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)

screen = Screen()
screen.exitonclick()
