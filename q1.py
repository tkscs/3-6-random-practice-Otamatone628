
import random

def spin_twister_spinner():
  """
  Returns a list with a random color, side, and appendage
  
  colors: "red", "green", "yellow", or "blue"
  sides: "left" or "right"
  appendage: "hand" or "foot"
  """
  #YOUR CODE HERE
  sides = ["left", "right"]
  appendage = ["hand", "foot"]
  colors = ["red", "yellow", "green", "blue"]
  return random.choice(sides) + " " + random.choice(appendage) + " " + random.choice(colors)

# Here's the function call. This should print a random assortment of twister commands
for _ in range(10):
  print(spin_twister_spinner())