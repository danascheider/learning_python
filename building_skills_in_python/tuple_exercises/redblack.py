import random

n= random.randrange(38)
if n == 0:
  print '0', 'green'
elif n == 37:
  print '00', 'green'
elif n in (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36):
  print n, 'red'
else:
  print n, 'black'