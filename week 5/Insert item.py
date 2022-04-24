numL = list(map(int, input().split()))
numS = list(map(int, input().split()))
numL.append(numS[1])
for i in range(len(numL) - 1, numS[0], -1):
    numL[i], numL[i - 1] = numL[i - 1], numL[i]
print(' '.join(map(str, numL)))
