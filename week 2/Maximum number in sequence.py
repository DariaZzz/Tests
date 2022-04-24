n = int(input())
maxN = n
while n != 0:
    n = int(input())
    if n > maxN and n != 0:
        maxN = n
print(maxN)
