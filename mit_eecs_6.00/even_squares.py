def evenSquares(lst):
  newList = []

  for value in lst:
    if value % 2 == 0:
      newList.append(value ** 2)