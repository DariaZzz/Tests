numL = list(map(int, input().split()))
maxN = numL[0]
k = 0
for i in range(1, len(numL)):
    if numL[i] > maxN:
        maxN = numL[i]
        k = i
print(maxN, k)
