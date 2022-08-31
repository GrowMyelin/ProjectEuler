# Problem 52 - Permuted Multiples

def containsDigits(x,*args):
    contains = True
    for a in args:
        if all(a_item in str(x) for a_item in str(a)):
            pass
        else:
            contains = False
    return contains

found = False
i = 1
while not found:
    if containsDigits(i,2*i,3*i,4*i,5*i,6*i):
        print(i)
        found = True
    else:
        i += 1
