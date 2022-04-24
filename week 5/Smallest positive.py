numList = list(map(int, input().split()))
minN = numList[0]
k = 1
while minN <= 0:
    minN = numList[k]
    k += 1
for i in range(1, len(numList)):
    if 0 < numList[i] < minN:
        minN = numList[i]
print(minN)
