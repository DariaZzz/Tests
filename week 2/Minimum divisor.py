"""
Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
 Формат ввода
Вводится целое положительное число.
 Формат вывода
Выведите ответ на задачу.
"""
n = int(input())
i = n
minDiv = n
while i > 1:
    if n % i == 0 and i < minDiv:
        minDiv = i
    i -= 1
print(minDiv)
