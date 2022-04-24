from math import sqrt


def IsPrime(n):
    k = 2
    while k <= sqrt(n):
        if n % k == 0:
            return False
        k += 1
    return True


n1 = int(input())
n1 = IsPrime(n1)
if n1 == 1:
    print('YES')
else:
    print('NO')
