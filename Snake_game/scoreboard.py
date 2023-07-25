from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.score = 0
    with open("C:/Users/Mike Nwabudike/Documents/Python_Learn/Udemy/100 Days of Code/Day_20-21 - Snake_game/data.txt", "r") as data:
       self.high_score = int(data.read())
    self.color("white")
    self.pu()
    self.goto(0, 270)
    self.write(f"Score: {self.score}", align= ALLIGNMENT, font = FONT)
    self.hideturtle()
    self.update_scoreboard()
    
  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score}   High Score: {self.high_score}", align= ALLIGNMENT, font = FONT)
    
  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("C:/Users/Mike Nwabudike/Documents/Python_Learn/Udemy/100 Days of Code/Day_20-21 - Snake_game/data.txt", "w") as data:
        data.write(f"{self.high_score}")
    self.score = 0
    self.update_scoreboard()
  
  #def game_over(self):
  #  self.goto(0, 0)
  #  self.write(f"GAME OVER.", align= ALLIGNMENT, font = FONT)
    
  def increase_score(self):
    self.score += 1
    self.update_scoreboard()