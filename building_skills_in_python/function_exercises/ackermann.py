# Ackermann's function is an extremely complex algorithm that computes some really
# big results. This is a function which is specifically designed to be complex.
# It cannot be rewritten as a simple loop. Further, it produces extremely large
# results because it describes extremely large exponents.
#
# Ackermann's function has two numbers, m and n.
# 1. Base Case: If m = 0, return n + 1
# 2. N Zero Case: If m != 0 and n = 0, return ackermann(m - 1, 1)
# 3. N Non-Zero Case: if m = 0 and n = 0, return ackermann(m - 1, ackermann(m, n - 1))

def ackermann(m, n):
  if m == 0:
    return n + 1
  elif n == 0:
    return ackermann(m - 1, 1)
  elif n != 0:
    return ackermann(m - 1, ackermann(m, n - 1))

print 'Enter two numbers: '
first  = int(raw_input())
second = int(raw_input())

print 'The Ackermann function value is %d.' % (ackermann(first, second))