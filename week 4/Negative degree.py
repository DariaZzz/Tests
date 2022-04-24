def power(a, n):
    sumP = 1
    if n > 0:
        while n != 0:
            sumP *= a
            n -= 1
    elif n < 0:
        while n != 0:
            sumP *= 1 / a
            n += 1
    return sumP


a1, n1 = float(input()), int(input())
print(power(a1, n1))
