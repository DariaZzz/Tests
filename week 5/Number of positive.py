numList = list(map(int, input().split()))
sumN = 0
for i in range(len(numList)):
    if numList[i] > 0:
        sumN += 1
print(sumN)
