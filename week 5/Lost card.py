n = int(input())
sumN = 0
for i in range(n + 1):
    sumN += i
for i in range(n - 1):
    k = int(input())
    sumN -= k
print(sumN)
