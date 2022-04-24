numL = list(map(int, input().split()))
i = len(numL) - 1
while i > -1:
    if numL[i] == 0:
        numL.pop(i)
        numL.append(0)
    else:
        i -= 1
print(*numL)
