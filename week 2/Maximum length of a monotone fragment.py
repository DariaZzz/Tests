n = int(input())
now = n
k = 1
maxK = 0
s = 0
while n != 0:
    n = int(input())
    if n > now and s == 0 and n != 0:
        s = 1
    elif n < now and s == 0 and n != 0:
        s = -1
    if n > now and s == 1:
        k += 1
        if k > maxK:
            maxK = k
    elif n < now and s == -1 and n != 0:
        k += 1
        if k > maxK:
            maxK = k
    elif n > now and s == -1 and n != 0:
        if k > maxK:
            maxK = k
        k = 2
        s = 1
    elif n < now and s == 1 and n != 0:
        if k > maxK:
            maxK = k
        k = 2
        s = -1
    else:
        if k > maxK:
            maxK = k
        k = 1
        s = 0
    now = n
print(maxK + 0 ** maxK)
