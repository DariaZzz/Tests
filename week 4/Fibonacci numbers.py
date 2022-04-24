def phib_tail(a, b, n):
    if n == 0:
        return a
    else:
        return phib_tail(b, a + b, n - 1)


def phib(a):
    return phib_tail(0, 1, a)


a1 = int(input())
print(phib(a1))
