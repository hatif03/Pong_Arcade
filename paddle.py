from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):

    def __init__(self, coord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.speed("fastest")
        self.goto(coord)

    def move_up(self):
        self.speed("fastest")
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.speed("fastest")
        self.goto(self.xcor(), self.ycor() - 20)
