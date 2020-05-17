from random import randint
from random import seed
from datetime import datetime

class Die:
  """A generic class for a die with arbitrary sides"""
  def __init__(self, sides = 6):
    self.sides = sides
    self.seedFromTime = datetime.now()
    seed(self.seedFromTime)

  def roll(self):
    return randint(1,self.sides)