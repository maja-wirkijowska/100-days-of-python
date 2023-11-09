from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win?: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(6):
    temp_turtle = Turtle(shape="turtle")
    temp_turtle.penup()
    temp_turtle.color(colors[turtle_index])
    temp_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(temp_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You win! The {winner} tutle was first!")
            else:
                print(f"You lost! The {winner} tutle was first!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
