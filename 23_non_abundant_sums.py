# Problem 23 - Non-abundant sums
from sympy import divisors

def isAbundant(num):
    s = sum(divisors(num)[:-1])
    if s > num:
        return True
    else:
        return False

def isAbundantSum(num,abundants):
    for a in abundants:
        for b in abundants:
            if a+b==num:
                return True
    return False
abundants = []
nonAbundantSums = []
for i in range(28123):
    if isAbundant(i):
        abundants.append(i)
    if not isAbundantSum(i,abundants):
        nonAbundantSums.append(i)

print(nonAbundantSums)
print(sum(nonAbundantSums))
