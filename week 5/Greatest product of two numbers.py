numL = list(map(int, input().split()))
maxN = numL[0]
minN = numL[0]
secMax = numL[0]
secMin = numL[0]
maxK = 0
minK = 0
for i in range(len(numL)):
    if numL[i] > maxN:
        maxN = numL[i]
        maxK = i
    elif numL[i] < minN:
        minN = numL[i]
        minK = i
for i in range(len(numL)):
    if secMax <= numL[i] <= maxN and i != maxK:
        secMax = numL[i]
    elif secMin >= numL[i] >= minN and i != minK:
        secMin = numL[i]
if secMax * maxN > secMin * minN:
    print(secMax, maxN)
else:
    print(minN, secMin)
