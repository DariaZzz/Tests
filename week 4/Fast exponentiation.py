def power(a, n, acc=1):
    if n > 0:
        if n % 2 == 0:
            return power(a ** 2, n / 2, acc)
        else:
            return power(a, n - 1, acc * a)
    return acc


a1, b1 = float(input()), int(input())
print(power(a1, b1))
