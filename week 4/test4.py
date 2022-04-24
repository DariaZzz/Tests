def fExp(a, n):
    if n > 0:
        fExp(a, n - 1)
        return (a ** 2) ** (n / 2) * 0 ** (n % 2) +\
                a * a ** (n - 1) * 0 ** (n % 2 - 1)
    return 1


a1, b1 = float(input()), int(input())
print(fExp(a1, b1))
