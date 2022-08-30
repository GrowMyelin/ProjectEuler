# Problem 120 - Square Remainders
rmax = []
for i in range(3,1001):
    r = 2*i*((i-1) // 2)
    rmax.append(r)

print(sum(rmax))