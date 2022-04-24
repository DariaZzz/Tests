numL = list(map(int, input().split()))
x = int(input())
numL.append(x)
i = 0
finS = -1
s = len(numL) - 1
while s > 0 and i == 0:
    if numL[s] > numL[s - 1]:
        numL[s], numL[s - 1] = numL[s - 1], numL[s]
        finS = s - 1
    else:
        finS = s
        i = 1
    s -= 1
print(finS + 1)
