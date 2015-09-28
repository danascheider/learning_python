# Use a list comprehension to define a procedure, called sumAbsProd, that returns 
# the sum of the absolute values of the products of all the pairs of numbers where
# one is drawn from each of two input lists.
#
# Use the `sum` and `abs` built-in functions in Python.

def sumAbsProd(list1, list2):
  return sum([abs(x * y) for x in list1 for y in list2])