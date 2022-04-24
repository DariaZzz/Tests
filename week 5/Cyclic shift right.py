numL = list(map(int, input().split()))
now = numL[0]
for i in range(1, len(numL)):
    numL[i], now = now, numL[i]
numL[0] = now
print(*numL)
