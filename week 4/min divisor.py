from math import sqrt


def MinDivisor(n1):
    k = 2
    while k <= sqrt(n1):
        if n1 % k == 0:
            return k
        k += 1
    return n1


n = int(input())
print(MinDivisor(n))
