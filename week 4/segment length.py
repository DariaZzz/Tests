from math import sqrt


def slen(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        ans = abs(x2 - x1) + abs(y2 - y1)
    else:
        ans = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return ans


x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
print(slen(x1, y1, x2, y2))
