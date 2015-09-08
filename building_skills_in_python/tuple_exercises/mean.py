import math

# Computing the mean of a list of values is relatively simple. The mean is the sum of 
# the values divided by the number of values in the list. Write a function that finds
# the mean value in a tuple.

def mean(tup):
  s = 0

  for num in tup:
    s += num

  return float(s) / len(tup)

# The standard deviation can be done a few ways, but we'll use the formula shown below. 
# This computes a deviation measurement as the square of the difference between each 
# sample and the mean. The sum of these measurements is then divided by the number of 
# values times the number of degrees of freedom to get a standardized deviation measurement. 

def sdev(tup):
  xBar = mean(tup)
  s    = 0

  for num in tup:
    s += (num - xBar) ** 2

  return math.sqrt(float(s) / (len(tup) - 1))