import math

air_pressure_at_sea_level = 1.01325E5 # N/m**2
molecular_weight_of_air = 28.96E-3 # kg/mol
gas_constant = 8.314 # joule/(K*mol)
acceleration_of_gravity = 9.82 # m/s**2
elevation_in_meters = 840
ocean_area = 3.61E14 # m
land_area = 1.49E14

def temperature_in_kelvins(temperature_in_degrees_celsius):
  return 273 + temperature_in_degrees_celsius

def pressure_at_elevation(elevation, temperature_in_kelvins):
  exponent = molecular_weight_of_air * acceleration_of_gravity * elevation / (gas_constant * temperature_in_kelvins)
  return air_pressure_at_sea_level * math.exp(exponent)

def average_atmospheric_weight():
  return pressure_at_elevation(elevation_in_meters,15) * land_area + air_pressure_at_sea_level * ocean_area

print average_atmospheric_weight()