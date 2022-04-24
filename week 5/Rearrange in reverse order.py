numL = list(map(int, input().split()))
for i in range(len(numL) // 2):
    numL[i], numL[(len(numL) - 1) - i] = numL[(len(numL) - 1) - i], numL[i]
print(' '.join(map(str, numL)))
