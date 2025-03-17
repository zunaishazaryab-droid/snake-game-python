from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food


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
    

snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
     screen.update()
     time.sleep(0.1)
     snake.move()
     if snake.head.distance(food) < 15:
         print("noam noam")
    #  segments[0].left(90)
       
        












screen.exitonclick()