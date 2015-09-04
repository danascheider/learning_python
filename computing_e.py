import math

e = math.e
n = 1
i = 1
k = 1

while abs(e - k) > 0.000001:
  n *= i
  i += 1
  k += 1.0 / n

print k