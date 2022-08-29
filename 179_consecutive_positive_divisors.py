# Problem 179 - Consecutive Positive Divisors
import numba
import time
from sympy import divisors

@numba.jit(forceobj=True)
def divisorGenerator(n):
    large_divisors = []
    for i in range(1,int(n**0.5+1)):
        if n % i == 0:
            yield i
            if i*i !=n:
                large_divisors.append(n/i)
    for divisor in reversed(large_divisors):
        yield int(divisor)

count = 0
start = time.time()
maxVal = 10**7
for i in range(1,maxVal):
    nextVal = i+1
    a=len(divisors(i))
    b=len(divisors(nextVal))
    if a==b:
        count += 1
end = time.time()
print(count)
print(end-start)