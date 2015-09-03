import math

# Calculate the wind chill temperature, in degrees Fahrenheit, given a wind velocity (in miles per hour)
# and an air temperature (in degrees Fahrenheit) of temp

def wind_chill(speed, temp):
  return 35.74 + 0.6215 * temp - 35.75 * math.pow(speed, 0.16) + 0.4275 * temp * math.pow(speed, 0.16)

print wind_chill(15, -2)