a = input()
k = 0
while k < len(a):
    if k % 3 != 0:
        print(a[k], end='')
    k += 1
