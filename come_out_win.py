print 'Roll the first die: '
d1 = int(raw_input())

assert 1 <= d1 <= 6

print 'Roll the second die: '
d2 = int(raw_input())

assert 1 <= d2 <= 6

win    = bool(d1 + d2 == 7) | bool(d1 + d2 == 11)
loss   = bool(d1 + d2 == 2) | bool(d1 + d2 == 3) | bool(d1 + d2 == 12)
point  = not win and not loss
result = None

if win:
  result = 'won'
elif loss:
  result = 'lost'
else:
  result = 'scored a point'

print 'You rolled %d; you have %s.' % (d1 + d2, result)