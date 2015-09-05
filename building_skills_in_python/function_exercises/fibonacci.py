print 'Enter an integer greater than or equal to 0: '
num = int(raw_input())

def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else: 
    for i in range(2, num + 1):
      return n + fib(n - 1)

print 'The %dth Fibonacci number is %d.' % (num, fib(num))