import math

air_pressure_at_sea_level = 1.01325E5 # N/m**2
acceleration_of_gravity = 9.82 # m/s**2
average_radius_of_earth = 6.37E6 # m
earth_surface_area = math.pow(average_radius_of_earth, 2) * math.pi * 4 # m**2

def mass_of_the_atmosphere(): # in kg/m**2
  return air_pressure_at_sea_level * acceleration_of_gravity * earth_surface_area

print air_pressure_at_sea_level * acceleration_of_gravity * earth_surface_area