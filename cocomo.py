# The COCOMO estimating model is used to estimate the cost and effort, measured in staff-months,
# required to write an application with K * 1000 lines of code.
#
# The relationship between lines of code and effort is modeled by the equation
#                     E = 2.4 * K ** 1.05
#
# The cost of the project is then derived from the estimated effort multiplied by the billing
# rate R:
#                     C = E * R * 152
#
# The project duration D, in calendar months, can be likewise derived from E:
#                     D = 2.5 * E ** 0.38
#
# Finally, staffing need S is modeled by 
#                     S = E / D

R = 150 # $/staff-hour

print "| Lines of Code | Effort (in staff-months) | Cost (in USD) | Duration (in months) | Staffing Need |"

for K in range(8, 65, 8):
  lines = K * 1000
  E = 2.4 * K ** 1.05
  C = E * R * 152
  D = 2.5 * E ** 0.38
  S = E / D

  print "| %d         | %d                      | %d      | %d                     | %d             |" % (lines, E, C, D, S)