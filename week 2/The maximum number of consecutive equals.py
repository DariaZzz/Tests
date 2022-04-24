n = int(input())
now = n
k = 1
maxK = 0
while n != 0:
    n = int(input())
    if n == now:
        k += 1
    else:
        if k > maxK:
            maxK = k
        k = 1
    now = n
print(maxK)
