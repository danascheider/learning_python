# Given the wind speed V in miles per hour and the temperature T in degrees Fahrenheit,
# the wind chill w may be modeled by the following formula, valid for wind speeds up to
# 40 mph:
#         35.74 + 0.6215 * T - 35.75 * V ** 16 + 0.4275 * T * V ** 0.16

print "| Temperature | Wind Speed | Wind Chill |"

def windChill(t,v):
  return 35.74 + 0.6215 * t - 35.75 * pow(v, 0.16) + 0.4275 * t * pow(v, 0.16)

for T in range(-10, 41, 5):
  for V in range(0, 41, 5):
    print "| %d         | %d          | %d        |" % (T, V, windChill(T,V))
