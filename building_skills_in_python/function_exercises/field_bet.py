import random

def win(dice, num, pays=1):
  if dice == num:
    return pays

  return 0

def field(dice):
  if (dice == 2) | (dice == 12):
    return win(dice, 2, 2) | win(dice, 12, 2)
  else:
    for val in [3, 4, 9, 10, 11]:
      if win(dice, val):
        return win(dice, val)
      else:
        pass

  return 0

def roll():
  val1, val2 = random.randint(2, 6), random.randint(0, 7)
  return val1 + val2

def play():
  dice = roll()
  print dice
  return field(dice)

print play()