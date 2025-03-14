from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("Welcome to Snake game")

goto = 0
for _ in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.setposition(x= 0 - goto, y= 0)
    goto +=20 
    














screen.exitonclick()