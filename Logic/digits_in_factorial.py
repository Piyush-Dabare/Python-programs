import math

def digitfactorial(n):
    d = 0
    for i in range(2,n+1):
        d += math.log10(i)
    return math.floor(d)+1

print(digitfactorial(6))
