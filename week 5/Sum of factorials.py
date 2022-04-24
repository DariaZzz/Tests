n = int(input())
sumN = 0
fact = 1
for k in range(1, n + 1):
    fact *= k
    sumN += fact
print(sumN)
