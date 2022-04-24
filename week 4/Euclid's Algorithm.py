def gcd(a, b):
    while a % b != 0:
        return gcd(b, a % b)
    return b


a1, b1 = int(input()), int(input())
print(gcd(a1, b1))
