def power(a, n, acc=1):
    if n > 0:
        return power(a, n - 1, acc * a)
    return acc


a1, n1 = float(input()), int(input())
print(power(a1, n1))
