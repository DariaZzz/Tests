x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
ans1 = 'b'
ans2 = 'a'
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
if y2 > y1 and ans1 == ans2:
    if y2 == y1 + 1:
        if x1 - 1 == x2 or x2 == x1 + 1:
            print('YES')
        else:
            print('NO')
    elif y2 == y1 + 2:
        if x1 - 2 <= x2 <= x1 + 2:
            print('YES')
        else:
            print('NO')
    elif y2 == y1 + 3:
        if x1 - 3 <= x2 <= x1 + 3:
            print('YES')
        else:
            print('NO')
    elif y2 == y1 + 4:
        if x1 - 4 <= x2 <= x1 + 4:
            print('YES')
        else:
            print('NO')
    elif y2 == y1 + 5:
        if x1 - 5 <= x2 <= x1 + 5:
            print('YES')
        else:
            print('NO')
    elif y2 == y1 + 6:
        if x1 - 6 <= x2 <= x1 + 6:
            print('YES')
        else:
            print('NO')
    elif y2 == y1 + 7:
        if x1 - 7 <= x2 <= x1 + 7:
            print('YES')
        else:
            print('NO')
else:
    print('NO')
