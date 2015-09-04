sacr = 15

print 'Enter the starting pressure: '
s = float(raw_input())

print 'Enter final pressure: '
f = float(raw_input())

print '| Depth | Time |'

def diveTime(s, f, c, d):
  return 33 * (s - f) / (c * (d + 33))

for d in range(30, 121, 10):
  print '| %d    | %d   |' % (d, diveTime(s, f, sacr, d))