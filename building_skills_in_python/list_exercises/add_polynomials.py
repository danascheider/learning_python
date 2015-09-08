def addPolynomials(p, q):
  resultSize, resultList = max(len(p), len(q)), []

  if len(p) < resultSize:
    numZeros = resultSize - len(p)
    lst = [0] * numZeros
    p1, q1 = tuple(lst) + p, q
  elif len(q) < resultSize:
    numZeros = resultSize - len(q)
    lst = [0] * numZeros
    q1, p1 = tuple(lst) + q, p
  else:
    p1, q1 = p, q

  for i in enumerate(p1):
    resultList.append(i[1] + q1[i[0]])

  return tuple(resultList)