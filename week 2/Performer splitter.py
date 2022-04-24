a = int(input())
b = int(input())
while a != b:
    if a % 2 == 1 and a > b or a // 2 < b:
        a = a - 1
        print('-1')
    elif a % 2 == 0 and a // 2 >= b:
        a = a // 2
        print(':2')
