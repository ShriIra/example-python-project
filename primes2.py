from mynumbers.factors import getFactors

from mynumbers import factors

def isPrime(n, foundPrimes=None):
    return len(getFactors(n)) == 2

print(isPrime(5))

print("in primes2.py the name is: ", __name__)