numL = list(map(int, input().split()))
k = 0
for i in range(1, len(numL) - 1):
    if numL[i - 1] < numL[i] and numL[i] > numL[i + 1]:
        k += 1
print(k)
