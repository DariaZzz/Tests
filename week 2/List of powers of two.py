"""
По данному числу N распечатайте все целые степени двойки, не превосходящие N,
в порядке возрастания.Операцией возведения в степень пользоваться нельзя!
 Формат ввода
Вводится натуральное число.
 Формат вывода
Выведите ответ на задачу.
"""
n = int(input())
i = 0
k2 = 0
ans = 1
print(ans, end=' ')
while i <= n:
    while k2 <= i:
        ans *= 2
        k2 += 1
    if ans <= n:
        print(ans, end=' ')
    else:
        break
    i += 1