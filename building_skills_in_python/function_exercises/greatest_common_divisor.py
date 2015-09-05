print "Enter two numbers:"
first = int(raw_input())
second = int(raw_input())

def gcd(p, q):
  if (p == q):
    return p
  elif p < q:
    return gcd(q, p)
  elif p > q:
    return gcd(q, p-q)


print "The greatest common divisor of %d and %d is %d" % (first, second, gcd(first, second))