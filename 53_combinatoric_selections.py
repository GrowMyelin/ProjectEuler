# Problem 53 - Combinatoric Selections
import math
mills = 0
for n in range(1,101,1):
    for r in range(1,n,1):
        if math.comb(n,r) > 1000000:
            mills += 1

print(mills)