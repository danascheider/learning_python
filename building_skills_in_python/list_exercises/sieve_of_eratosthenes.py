# This is an algorithm which locates prime numbers. A prime number can only be
# divided evenly by 1 and itself. We locate primes by making a table of all 
# numbers, and then crossing out the numbers which are multiples of other
# numbers. What is left must be prime.

def sieveOfEratosthenes():
  prime = [True] * 5000
  p = 2

  while 2 <= p < 5000:
    if prime[p]:
      k = p + p

      while k < 5000:
        prime[k] = False
        k += p

    if prime[p]:
      print p

    p += 1

sieveOfEratosthenes()