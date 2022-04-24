def IsPointInSquare(x, y):
    return (-1 <= x <= 1) * (-1 <= y <= 1)


x, y = float(input()), float(input())
ans = IsPointInSquare(x, y)
if ans == 1:
    print('YES')
else:
    print('NO')
