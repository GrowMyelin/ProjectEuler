# Problem 38 - Pandigital Multiples

def pandigital(num):
    pdigit = ''
    c = 0
    while len(pdigit) < 9:
        c += 1
        pdigit += str(num*c)
    if len(pdigit)==9 and '1' in pdigit and '2' in pdigit \
        and '3' in pdigit and '4' in pdigit and '5' in pdigit \
        and '6' in pdigit and '7' in pdigit and '8' in pdigit \
        and '9' in pdigit:
        return pdigit
    else:
        return '0'

pdigits = []
for i in range(1,10000000):
    pdigits.append(int(pandigital(i)))

print(max(pdigits))