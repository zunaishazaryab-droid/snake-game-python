from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")
screen.title("Welcome to Snake game")
screen.tracer(0)

# goto = 0
# for _ in range(3):
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.setposition(x= 0 - goto, y= 0)
#     goto +=20 
    
starting_position = [(0,0), (-20, 0), (-40, 0)]
segments = []


for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


is_game_on = True


while is_game_on:
     screen.update()
     time.sleep(1)
     for seg in segments:
        seg.forward(20)
       
        












screen.exitonclick()