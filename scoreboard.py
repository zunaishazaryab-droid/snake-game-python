from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 17, 'normal')


class ScoreBoard(Turtle):
    
    
    def __init__(self):
        file = open("data.txt", mode="r")
        content = file.read()
        
        super().__init__()
        self.score = 0
        self.high_score = int(content)
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.update_Score()
        file.close()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="Game Over", align=ALIGNMENT, font=FONT)
    
    def reset(self):
        file = open("data.txt", mode="w")
        
        
        if(self.score > self.high_score):
            self.high_score = self.score
            file.write(str(self.high_score))
            file.close()
        self.score = 0
        self.update_Score()
    
    def increase_score(self):
        self.score += 1
        self.update_Score()
        
    def update_Score(self):
       
        self.clear()
        self.write(arg=f"Score {self.score} High Score is {self.high_score}", align=ALIGNMENT, font=FONT)