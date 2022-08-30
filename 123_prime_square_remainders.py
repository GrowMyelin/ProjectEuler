# Problem 123 - Prime Square Remainders
from sympy import prime

n = 3
x = prime(n)

def remainder(n):
    x = prime(n)
    return (((x-1)**n)+((x+1)**n)) % (x**2)

for i in range(9593,100000):
    if remainder(i) > 10**10:
        print(i)
        break



""" 
Finds minimum value.
r = 0
for n in range(1,10000):
    x = prime(n)
    if x**2 > 10**10:
        print(n)
        break """
