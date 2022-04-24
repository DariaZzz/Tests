"""
Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES,
а если в разные цвета – то NO.
Формат ввода
Вводятся 4 числа - координаты клеток.
Формат вывода
Выведите ответ на задачу.
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if y1 % 2 == 1:
    if x1 % 2 == 1:
        ans1 = 1
    else:
        ans1 = 0
else:
    if x1 % 2 == 0:
        ans1 = 1
    else:
        ans1 = 0
if y2 % 2 == 1:
    if x2 % 2 == 1:
        ans2 = 1
    else:
        ans2 = 0
else:
    if x2 % 2 == 0:
        ans2 = 1
    else:
        ans2 = 0
if ans1 == ans2:
    print('YES')
else:
    print('NO')
