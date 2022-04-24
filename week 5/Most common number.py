numL = list(map(int, input().split()))
maxCount = numL[0]
if len(numL) > 1:
    for i in range(len(numL)):
        if numL.count(numL[i]) > numL.count(maxCount):
            maxCount = numL[i]
print(maxCount)
