import random, time

random.seed(time.clock())
print random.randrange(6), random.randrange(6)
print random.randrange(1, 7), random.randrange(1, 7)
print random.randrange(2, 37, 2)
print random.randrange(1, 36, 2)