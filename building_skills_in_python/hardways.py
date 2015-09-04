print 'Roll the first die: '
d1 = int(raw_input())

assert 1 <= d1 <= 6

print 'Roll the second die: '
d2 = int(raw_input())

assert 1 <= d1 <= 6

if d1 == d2 and d1 + d2 > 3:
  print 'You rolled a %d and won the hard way!' % (d1 + d2)
else:
  print 'You rolled a %d lost...the hard way!' % (d1 + d2)
