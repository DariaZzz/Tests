numL = list(map(int, input().split()))
for i in range(0, (len(numL) // 2 * 2) - 1, 2):
    numL[i], numL[i + 1] = numL[i + 1], numL[i]
print(*numL)
