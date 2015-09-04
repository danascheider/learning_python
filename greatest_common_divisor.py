p = 81
q = 45

while p != q:
  original_p, original_q = p, q

  if p < q:
    p, q = original_q, original_p
  elif p > q:
    p = p - q

print p