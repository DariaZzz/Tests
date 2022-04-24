def IsPointInArea(x, y):
    if (y >= -x and y >= 2 * x + 2 and \
            (y - 1) ** 2 <= 4 - (x + 1) ** 2)\
            or (y <= -x and y <= 2 * x + 2 and\
            (y - 1) ** 2 <= 4 - (x + 1) ** 2):
        return True
    return False


x1, y1 = float(input()), float(input())
if IsPointInArea(x1, y1) == 1:
    print('YES')
else:
    print('NO')
