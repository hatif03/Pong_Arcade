from turtle import Turtle, Screen

screen = Screen()

class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(1, 1)
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed("fastest")
        self.home()
        self.xmove = 10
        self.ymove = 10
        self.sec = 0.1

    def move(self):
        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)

    def bounce(self):
        self.ymove *= -1
        self.sec *= 0.9

    def paddle_bounce(self):
        self.xmove *= -1
        self.sec *= 0.9

    def reset_position(self):
        self.home()
        self.sec = 0.1
        self.paddle_bounce()
        screen.update()
