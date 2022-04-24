"""
Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
Даны две различные клетки шахматной доски, определите,
может ли король попасть с первой клетки на вторую одним ходом.
 Формат ввода
Программа получает на вход четыре числа от 1 до 8 каждое,
задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
 Формат вывода
Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую
или NO в противном случае.
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x2 == x1:
    if y2 == y1 + 1 or y2 == y1 - 1:
        print('YES')
    else:
        print('NO')
elif x2 == x1 + 1:
    if y2 == y1 + 1 or y2 == y1 - 1 or y2 == y1:
        print('YES')
    else:
        print('NO')
elif x2 == x1 - 1:
    if y2 == y1 + 1 or y2 == y1 - 1 or y2 == y1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
