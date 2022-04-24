from math import sqrt
n = int(input())
k = 1
sumN = n
stDev = n ** 2
while n != 0:
    n = int(input())
    k += 1
    sumN += n
    stDev += (n - sumN / k) ** 2
stDev = sqrt(stDev) / (k - 1)
print(stDev)
