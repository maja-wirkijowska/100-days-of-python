from turtle import Turtle, Screen


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def turn_right():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)


def turn_left():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)


def clear():
    turtle.home()
    turtle.clear()


turtle = Turtle()

screen = Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
