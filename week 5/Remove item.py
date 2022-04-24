numL = list(map(int, input().split()))
k = int(input())
for i in range(k, len(numL) - 1):
    numL[i], numL[i + 1] = numL[i + 1], numL[i]
numL.pop()
print(' '.join(map(str, numL)))
