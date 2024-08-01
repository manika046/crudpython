import random

options = ['Rock', 'Paper', 'Scissors']

class RockPaperScissors:
  def __init__(self):
    pass
  
  def computer(self):
    return random.choice(options)
  
  def user(self, umove, cmove):
    if umove == cmove:
      return "It's a tie!"
    elif (umove == 'Rock' and cmove == 'Scissors') or (umove == 'Paper' and cmove == 'Rock') or (umove == 'Scissors' and cmove == 'Paper'):
      return "You win!"
    else:
      return "You lose!"
    
  def play(self):
    while True:
      print("\n Choose (Rock, Paper, Scissor) or 'quit' to exit:")
      umove = input().capitalize()
      
      if umove == 'Quit':
        print("Thanks for playing")
        break
    
      if umove not in options:
        print("Invalid Choice")
        continue
    
      cmove = self.computer()
      print(f"Computer chose... {cmove}")
      result = self.user(umove, cmove)
      print(result)
    
game = RockPaperScissors()
game.play()