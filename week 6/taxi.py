numKm = list(map(int, input().split()))
numT = list(map(int, input().split()))
numKm.sort()
numT.sort(reverse=True)
sumN = 0
for i in range(len(numKm)):
    sumN += numKm[i] * numT[i]
print(sumN)
