numL = list(map(int, input().split()))
sumK = 0
for i in range(len(numL)):
    for c in range(i + 1, len(numL)):
        if numL[i] == numL[c]:
            sumK += 1
print(sumK)
