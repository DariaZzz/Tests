n = int(input())
maxN = n
k = 1
while n != 0:
    n = int(input())
    if n != 0:
        if n > maxN:
            maxN = n
            k = 1
        elif n == maxN:
            k += 1
print(k)
