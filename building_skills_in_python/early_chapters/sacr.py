def sacr(depth, starting_pressure, final_pressure, time):
  return 33 * (starting_pressure - final_pressure) / (time * (depth + 33))

def max_time(depth, starting_pressure, final_pressure, sacr):
  return 33 * (starting_pressure - final_pressure) / (sacr * (depth + 33))

print 'SACR for a Shallow Dive: %d' % sacr(30, 3000, 1500, 60)
print 'SACR for a Medium Dive: %d' % sacr(60, 3000, 500, 60)
print 'SACR for a Deep Dive: %d' % sacr(100, 3000, 500, 15)

print 'Maximum Time at 60 ft: %d minutes' % max_time(60, 2500, 500, 15.2)
print 'Maximum Time at 70 ft: %d minutes' % max_time(70, 2500, 500, 15.2)