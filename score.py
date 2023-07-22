from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def display(self):
        self.clear()
        self.goto(-50, 200)
        self.write(self.l_score, align="left", font=("Comic Sans MS", 30, "bold"))
        self.goto(50, 200)
        self.write(self.r_score, align="right", font=("Comic Sans MS", 30, "bold"))

    def l_win(self):
        self.l_score += 1

    def r_win(self):
        self.r_score += 1

    def win(self):
        if self.r_score == 5:
            self.home()
            self.write("Right Player Wins!", align="center", font=("Comic Sans MS", 50, "bold"))
            return False
        elif self.l_score == 5:
            self.home()
            self.write("Left Player Wins!", align="center", font=("Comic Sans MS", 50, "bold"))
            return False
        else:
            return True
