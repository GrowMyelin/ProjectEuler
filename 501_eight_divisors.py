# 501 - Eight Divisors

import time
import numpy as np
import numba as nb

@nb.njit('List(int64)(int64)')
def get_prime_divisors(n):
    divisors = []
    while n % 2 == 0:
        divisors.append(2)
        n //= 2
    while n % 3 == 0:
        divisors.append(3)
        n //= 3
    i = 5
    while i*i <= n:
        for k in (i, i+2):
            while n % k == 0:
                divisors.append(k)
                n //= k
        i += 6
    if n > 1:
        divisors.append(n)
    return divisors

@nb.njit('List(int64)(int64)')
def get_divisors(n):
    divisors = []
    if n == 1:
        divisors.append(1)
    elif n > 1:
        prime_factors = get_prime_divisors(n)
        divisors = [1]
        last_prime = 0
        factor = 0
        slice_len = 0
        # Find all the products that are divisors of n
        for prime in prime_factors:
            if last_prime != prime:
                slice_len = len(divisors)
                factor = prime
            else:
                factor *= prime
            for i in range(slice_len):
                divisors.append(divisors[i] * factor)
            last_prime = prime
    return divisors

@nb.njit()
def f(n):
    # count of numbers <= n with exactly 8 divisors
    c = 0
    for i in range(n+1):
        if len(get_divisors(i))==8:
            c += 1
    return c
start = time.time()
print(f(10**12))
end = time.time()
print(end-start)
