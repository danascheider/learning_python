# Computing the mean of a list of values is relatively simple. The mean is the sum of 
# the values divided by the number of values in the list. Write a function that finds
# the mean value in a tuple.

def mean(tup):
  s = 0

  for num in tup:
    s += num

  return float(s) / len(tup)