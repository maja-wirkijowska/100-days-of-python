from turtle import Turtle, Screen

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")

divider = Turtle()
divider.color("white")
divider.right(90)
while divider.ycor() < -300:
    divider.pendown()
    divider.forward(10)
    divider.penup()
    divider.forward(10)

screen.exitonclick()
