print "Enter a number between 1 and 30:"
n = int(raw_input())

while n != 1:
  if n % 2:
    n = n * 3 + 1
  else:
    n /= 2

  print n