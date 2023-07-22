from turtle import Turtle, Screen
from paddle import Paddle
from pong import Pong
import time
from score import Score


screen= Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=500)
screen.title("Pong_Arcade Game")
screen.tracer(0)
l = (-430, 0)
r = (430, 0)
r_paddle = Paddle(r)
l_paddle = Paddle(l)
ball = Pong()
scr = Score()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.sec)
    screen.update()
    ball.move()
    scr.display()

    if ball.ycor() == 230 or ball.ycor() == -230:
        ball.bounce()

    if ball.xcor() > 400 or ball.xcor() < -400:
        if ball.distance(r_paddle) <= 50 or ball.distance(l_paddle) <= 50:
            ball.paddle_bounce()

    if ball.xcor() > 450:
        ball.reset_position()
        scr.l_win()

    if ball.xcor() < -450:
        ball.reset_position()
        scr.r_win()


    game_is_on = scr.win()





screen.exitonclick()