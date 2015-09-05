print 'Enter an integer greater than or equal to zero: '
num = int(raw_input())

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

print '%d! = %d' % (num, factorial(num))