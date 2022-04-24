from math import sqrt


def IsPointInSquare(x, y):
    return (-1 <= x <= 1 and y == 0) or (-1 <= y <= 1 and x == 0)\
           or (-1 < x < 1 and -1 < y < 1 and
               (sqrt(x ** 2 + y ** 2) <= sqrt(2) / 2))


x, y = float(input()), float(input())
ans = IsPointInSquare(x, y)
if ans != 0:
    print('YES')
else:
    print('NO')
