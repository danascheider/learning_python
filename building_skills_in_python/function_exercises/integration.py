def f(x):
  return x ** 2

def integrate(func, a, b, s=0.5):
  x = a
  h = (b - a) / s
  val = 0.0

  while a <= x < b:
    print "val = %d, x = %d" % (val, x)
    val += func(x) * h
    x += h

  return val

print integrate(f, 7, 10)