print 'Enter a number: '
x = float(raw_input())

print 'Enter another number: '
y = float(raw_input())

print 'Enter a third number: '
z = float(raw_input())

list = [x, y, z]

if list[0] > list[1]:
  first, second = list[0], list[1]
  list[0] = second
  list[1] = first

if list[1] > list[2]:
  first, second = list[1], list[2]
  list[1] = second
  list[2] = first

if list[0] > list[1]:
  first, second = list[0], list[1]
  list[0] = second
  list[1] = first

print list