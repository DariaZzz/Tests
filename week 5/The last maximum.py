numList = list(map(int, input().split()))
maxN = numList[0]
ind = 0
for i in range(1, len(numList)):
    if numList[i] >= maxN:
        maxN = numList[i]
        ind = i
print(maxN, ind)
