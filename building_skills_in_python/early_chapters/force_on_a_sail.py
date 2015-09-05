# Calculate the force exerted on a sailboat by a sail of `area` square feet and a wind
# of `wind_speed` miles per hour.

def force_on_sail(area, wind_speed):
  return wind_speed ** 2 * 0.004 * area

print 'Force = %d units' % force_on_sail(61, 15)