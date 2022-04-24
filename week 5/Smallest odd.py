numList = list(map(int, input().split()))
minOdd = numList[0]
k = 1
while minOdd % 2 == 0:
    minOdd = numList[k]
    k += 1
for i in range(1, len(numList)):
    if numList[i] < minOdd and numList[i] % 2 != 0:
        minOdd = numList[i]
print(minOdd)
