def gcd(a, b):
    while a % b != 0:
        return gcd(b, a % b)
    return b


def ReduceFraction(n, m):
    while gcd(n, m) != 1:
        return n // gcd(n, m), m // gcd(n, m)
    return n, m


n1, m1 = int(input()), int(input())
print(*ReduceFraction(n1, m1))
