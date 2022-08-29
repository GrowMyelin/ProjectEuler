# Problem 32 - Pandigital Products
from sympy import divisors
def isPandigital(num,n):
    sNum = str(num)
    isP = True
    for i in range(1,n+1):
        if sNum.count(str(i))!=1:
            isP = False
        elif '0' in sNum:
            isP = False
    return isP
pp = []
for i in range(1,100000):
    div = divisors(i)
    for d in div:
        for dd in div:
            if d*dd == i:
                div.remove(d)
                x = str(d)+str(dd)+str(i)
                if isPandigital(x,9):
                    pp.append(i)
                    
pp = list(set(pp))
print(pp)
print(sum(pp))