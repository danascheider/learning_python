def search(seq, tgt, lo, hi):
  if lo + 1 >= hi:
    return -1 # not found

  m = (lo + hi) / 2
  if seq[m] == tgt:
    return m
  elif seq[m] > tgt:
    return search(seq, tgt, lo, m)
  elif seq[m] < tgt:
    return search(seq, tgt, m + 1, hi)