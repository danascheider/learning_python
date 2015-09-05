print "Enter a number greater than or equal to 2: "
number, p, c = float(raw_input()), 1, 2

while c < number:
  c *= 2
  p += 1

  if c * 2 > number:
    break

print p