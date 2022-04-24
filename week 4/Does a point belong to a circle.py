from math import sqrt


def SLen(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        ans = abs(x2 - x1) + abs(y2 - y1)
    else:
        ans = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return ans


def IsPointInCircle(x, y, xc, yc, r):
    return SLen(x, y, xc, yc) <= r


x, y, xc, yc, r = float(input()), float(input()), float(input()),\
                  float(input()), float(input())
ans = IsPointInCircle(x, y, xc, yc, r)
if ans != 0:
    print('YES')
else:
    print('NO')
