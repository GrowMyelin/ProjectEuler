# Problem 74 - Digit Factorial Chains
from math import factorial

def digitFactorial(n):
    s = 0
    for digit in str(n):
        s += factorial(int(digit))
    return s

def chain(n):
    ch = [n]
    nxt = digitFactorial(ch[-1])
    while nxt not in ch:
        ch.append(nxt)
        nxt = digitFactorial(ch[-1])
    return len(ch)
count = 0
for i in range(1,1000000):
    if chain(i)==60:
        count += 1

print(count)