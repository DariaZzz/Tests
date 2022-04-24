numL = list(map(int, input().split()))
maxN = numL[0]
minN = numL[0]
kMax = 0
kMin = 0
for i in range(1, len(numL)):
    if numL[i] > maxN:
        maxN = numL[i]
        kMax = i
    elif numL[i] < minN:
        minN = numL[i]
        kMin = i
numL[kMax], numL[kMin] = numL[kMin], numL[kMax]
print(*numL)
