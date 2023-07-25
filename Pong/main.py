from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()


screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
score = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))




'''paddle = Turtle("square")
paddle.color("white")
paddle.shapesize(stretch_wid= 5, stretch_len= 1)
paddle.pu()
paddle.goto(350, 0)


def go_up():
  new_y = paddle.ycor() + 20
  paddle.goto(paddle.xcor(), new_y)
  
def go_down():
  new_y = paddle.ycor() - 20
  paddle.goto(paddle.xcor(), new_y)'''

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()
  
  
  #detect collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()


  #detect collision with right paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()
    
  #detect r paddle misses
  if ball.xcor() > 380:
    ball.reset_position()
    score.l_point()

    #detect l paddle misses
  if ball.xcor() < -380:
    ball.reset_position()
    score.r_point()


screen.exitonclick()
