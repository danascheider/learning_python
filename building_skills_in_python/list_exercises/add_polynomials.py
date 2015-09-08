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

# I realize this code does not work. The examples in this book are a total clusterfuck.
# But I don't want to deal with correcting the multitude of errata and learning a new
# language at the same time, so there you go.

def multiplyPolynomials(p, q):
  resultSize = len(p) + len(q)
  resultList = [0] * resultSize

  for i in range(0, len(p)):
    for j in range(0, len(q)):
      resultList[i + j] = resultList[i + j] + p[i] * q[j]

  return tuple(resultList)

print multiplyPolynomials((1,), (2,))