def minn(a1, b1, c1, d1):
    min1 = min(a1, b1)
    min2 = min(c1, d1)
    min3 = min(min1, min2)
    print(min3)


a, b, c, d = int(input()), int(input()), int(input()), int(input())
minn(a, b, c, d)
