# Problem 55 - Lychrel Numbers

def addRev(n):
    rev = str(n)[::-1]
    return n+int(rev)

def isPalindrome(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False

def isLychrel(n):
    new = n
    for i in range(50):
        new = addRev(new)
        if isPalindrome(new):
            return False
    return True

count = 0
for i in range(10000):
    if isLychrel(i):
        count += 1
print(count)