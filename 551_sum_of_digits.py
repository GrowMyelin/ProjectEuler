# Problem 551 - Sum of Digits Sequence

a = 1
count = 0
s = 0
while count < 10**15:
    count += 1
    for i in str(a):
        s += int(i)
    a = s
print(count,a)