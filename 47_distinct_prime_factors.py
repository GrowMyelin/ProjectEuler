# Problem 47 - Distinct primes factors
import numba

@numba.jit
def checkPrime(num):
    isPrime = True
    for x in range(2,num,1):
        if num % x == 0:
            isPrime = False
    return isPrime

primes = []
for i in range(2,1000):
    if checkPrime(i):
        primes.append(i)


def returnFactors(num):
    factors = []
    frequencies = []
    for p in primes:
        if p >= num:
            break
        elif num % p == 0:
            if p not in factors:
                factors.append(p)
                count = 0
                n = num
                while n % p == 0:
                    count += 1
                    n = n // p
                frequencies.append(count)
    return [factors,frequencies]

def hasDistinctPrimes(amt,num):
    ff = returnFactors(num)
    if len(ff[1]) < amt:
        distinct = False
    else:
        distinct = True
    return distinct
count = 0
amt = 4
for i in range(1000000):
    if hasDistinctPrimes(amt,i):
        count += 1
    else:
        count = 0
    if count == amt:
        print(i-(amt-1))
        break


        






