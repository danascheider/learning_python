print "| Degrees C | Degrees F |"

def celsius_to_fahrenheit(c):
  return 32 + (212 - 32) * c / 100.0

def fahrenheit_to_celsius(f):
  return (f - 32) * 100 / float(212 - 32)

for C in range(-20, 31, 5):
  print "| %d       | %d         |" % (C, celsius_to_fahrenheit(C))

print "\n"

print "|Degrees F | Degrees C |"

for F in range(-10, 101, 5):
  print " %d        | %d         |" %(F, fahrenheit_to_celsius(F))