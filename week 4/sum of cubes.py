n = int(input())
s = n
i = n
num = 7
strN =' '
while i > 0 and num > 0 and s > 0:
    if s - i ** 3 >= 0:
        print(i ** 3, end=' ')
        s -= i ** 3
        num -= 1
    if i > 1:
        i -= 1
if num == 0:
    print(0)
