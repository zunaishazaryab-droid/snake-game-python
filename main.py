from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


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
    
score_board = ScoreBoard()
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
         snake.extends()
         score_board.update_Score()
         food.refresh()
    #  segments[0].left(90)
    
    # Detect the Collision with Wall
     if snake.head.xcor() > 282 or snake.head.xcor() < -282 or snake.head.ycor() > 282 or snake.head.ycor() < -282:
         is_game_on = False
         score_board.game_over()
    
    # Detect Collision with snake trail
     for segment in snake.segments:
         if segment == snake.head:
             pass
         elif snake.head.distance(segment) < 10:
             is_game_on = False
             score_board.game_over()
             
        
       
        












screen.exitonclick()