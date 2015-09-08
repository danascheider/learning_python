# Binary search requires input sequence to be sorted

def binarySearch(sequence, target):
  l, h = 0, len(sequence) - 1
  m = (l + h) / 2
  print "l=%d, h=%d, m=%d" % (l, h, m)

  if target == sequence[m]:
    return m
  else:
    while l + 1 < h and sequence[m] != target:
      print "l=%d, h=%d, m=%d" % (l, h, m)
      if target < sequence[m]:
        h = m
      elif target > sequence[m]:
        l = m + 1

      m = (l + h) / 2
      if target == sequence[m]:
        return m