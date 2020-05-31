from Die import Die

class Roller:
  """A class for doing various rolling operations related to 
  Dungeons and dragons"""
  def __init__(self):
    self.d20 = Die(20)
    self.d12 = Die(12)
    self.d8  = Die(8)
    self.d6  = Die(6)
    self.d4  = Die(4)

  def advantage(self):
    roll1 = self.d20.roll()
    roll2 = self.d20.roll()
    return max(roll1,roll2)

  def disadvantage(self):
    roll1 = self.d20.roll()
    roll2 = self.d20.roll()
    return min(roll1,roll2)

  def advdis(self):
    dis1 = self.disadvantage()
    dis2 = self.disadvantage()
    return max(dis1,dis2)

  def disadv(self):
    adv1 = self.advantage()
    adv2 = self.advantage()
    return min(adv1,adv2)

  def advdisadv(self):
    disadv1 = self.disadv()
    disadv2 = self.disadv()
    return max(disadv1,disadv2)

  def disdisadv(self):
    disadv1 = self.disadv()
    disadv2 = self.disadv()
    return min(disadv1,disadv2)

  def advadvdis(self):
    advdis1 = self.advdis()
    advdis2 = self.advdis()
    return max(advdis1,advdis2)

  def disadvdis(self):
    advdis1 = self.advdis()
    advdis2 = self.advdis()
    return min(advdis1,advdis2)