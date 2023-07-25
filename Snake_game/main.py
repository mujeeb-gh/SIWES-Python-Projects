from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
# setting up the screen
screen = Screen()
screen.bgcolor("black")
screen.textinput(title= "Welcome to Slittery Abyss", prompt= "Click ok to play")
screen.setup(width= 600, height= 600)
screen.title("Slithery Abyss")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()
  
  # detect collision with food
  if snake.head.distance(food) < 15:
    food.refresh()
    
    snake.extend()
    scoreboard.increase_score()
  
  # detect collision with wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    scoreboard.reset()
    snake.reset()
    
    
  # detect collision with taIl
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      scoreboard.reset()
      snake.reset()




screen.exitonclick()


  # do not ubderstand
'''for seg_num in range(len(segments) - 1, 0, -1):
    new_x = segments[seg_num - 1].xcor()
    new_y = segments[seg_num - 1].ycor()
    segments[seg_num].goto(new_x, new_y)
  
  segments[0].fd(20)
  segments[0].lt(90)'''