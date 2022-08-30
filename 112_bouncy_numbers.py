# Problem 112 - Bouncy Numbers

def isIncreasing(num):
    numList = list(str(num))
    for n in range(len(numList)-1):
        if int(numList[n]) <= int(numList[n+1]):
            pass
        else:
            return False
    return True

def isDecreasing(num):
    numList = list(str(num))
    for n in range(len(numList)-1):
        if int(numList[n]) >= int(numList[n+1]):
            pass
        else:
            return False
    return True

def isBouncy(num):
    if isIncreasing(num):
        return False
    elif isDecreasing(num):
        return False
    else:
        return True

count = 1
bouncyCount = 0
while bouncyCount / count < .99:
    count += 1
    if isBouncy(count):
        bouncyCount += 1
    

print(count)