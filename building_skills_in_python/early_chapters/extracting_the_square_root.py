print 'Pick a number greater than 1: '
number = float(raw_input())

g1 = 1.0
g2 = number

while abs(g1 * g1 - number) / number >= 0.001:
  midpoint = (g1 + g2) / 2.0
  comp = midpoint * midpoint - number

  if comp <= 0:
    g1 = midpoint
  
  if comp > 0:
    g2 = midpoint

print round(g1, 2)