from turtle import Turtle
 
class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.write(arg=f"Score {self.score}", align="center", font=('Arial', 17, 'normal'))
        
    def update_Score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score {self.score}", align="center", font=('Arial', 17, 'normal'))