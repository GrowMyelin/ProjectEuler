# Problem 56 - Digit Sum
import numba
@numba.jit(forceobj=True)
def digitSum(x):
    s = 0
    for dig in str(x):
        s += int(dig)
    return s

m = 0

for a in range(1,101,1):
    for b in range(1,101,1):
        m = max(m,digitSum(a**b))

print(m)