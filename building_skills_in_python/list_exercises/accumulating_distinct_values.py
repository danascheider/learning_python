# This exercise uses the bounded linear search algorithm to locate duplicate values
# in a sequence. This is a powerful technique to eliminate sorting from a wide variety
# of summary-type reports. Failure to use this algorithm leads to excessive processing
# in many types of applications.

def uniq(sequence):
  uniq = []

  for val in sequence:
    i = 0
    distinct = None

    uniq.append(val)

    while uniq[i] != val:
      i += 1

    if i != len(uniq) - 1:
      del uniq[-1]

  return uniq