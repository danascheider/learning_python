cars = 100                          # There are 100 cars to begin with
space_in_a_car = 4                  # Each car fits a driver and 3 passengers
drivers = 30                        # There are 30 drivers available
passengers = 90                     # 90 passengers need to be fit into the available cars

# The number of cars driven is equal to the number of drivers, but can't be more than the
# number of cars available.

cars_driven = min(cars, drivers)

# The number of cars not driven is equal to the number of available cars minus the number of
# cars being driven.

cars_not_driven = cars - cars_driven

carpool_capacity = cars_driven * space_in_a_car

# The average number of passengers per car accounts for the possibility that not every car
# is necessarily at capacity. Since it's a mean, you can have partial people.

average_passengers_per_car = float(passengers) / float(cars_driven)

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."