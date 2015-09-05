def f(x):
  return -5 * x * x + 2 * x - 3

def highest_function_value(minval, maxval):
  max = f(minval)

  for i in range(minval + 1, maxval + 1):
    if f(i) > max:
      max = f(i)

  return max

print highest_function_value(-10, 10)