import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.screensize(600, 600)
screen.title("PONG")
screen.tracer(0)

right_paddle = Paddle((300, 0))
left_paddle = Paddle((-300, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_running = True
while game_running:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 320 or ball.ycor() < -320:
        print("Y")
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 270 or ball.distance(left_paddle) < 50 and ball.xcor() < -270:
        print("X")
        ball.bounce_x()

    if ball.xcor() > 300:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -300:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
