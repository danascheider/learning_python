print 'Enter a number: '
num = float(raw_input())

print 'Enter a power: '
pwr = float(raw_input())

def odd(num):
  return num % 2

def fast_exponentiation(number, power):
  if power == 0:
    return 1.0
  elif odd(power):
    return number * fast_exponentiation(number, power - 1)
  else:
    t = fast_exponentiation(number, power / 2.0)
    return t * t

print (fast_exponentiation(num, pwr))