numL = list(map(int, input().split()))
maxN = numL[0]
minN = numL[0]
secMax = min(numL)
secMin = max(numL)
thiMax = min(numL)
maxK = 0
minK = 0
secMaxK = 0
secMinK = 0
if len(numL) == 3:
    for i in range(len(numL)):
        print(numL[i], end=' ')
elif len(numL) == 4:
    if numL[0] * numL[1] * numL[2] >= numL[0] * numL[1] * numL[3] and\
        numL[0] * numL[1] * numL[2] > numL[1] * numL[2] * numL[3] and\
            numL[0] * numL[1] * numL[2] >= numL[0] * numL[2] * numL[3]:
        print(numL[0], numL[1], numL[2])
    elif numL[0] * numL[1] * numL[3] >= numL[0] * numL[1] * numL[2] and\
        numL[0] * numL[1] * numL[3] >= numL[1] * numL[2] * numL[3] and\
            numL[0] * numL[1] * numL[3] >= numL[0] * numL[2] * numL[3]:
        print(numL[0], numL[1], numL[3])
    elif numL[1] * numL[2] * numL[3] >= numL[0] * numL[1] * numL[2] and\
        numL[1] * numL[2] * numL[3] >= numL[0] * numL[1] * numL[3] and\
            numL[1] * numL[2] * numL[3] >= numL[0] * numL[2] * numL[3]:
        print(numL[1], numL[2], numL[3])
    else:
        print(numL[0], numL[2], numL[3])
else:
    for i in range(len(numL)):
        if numL[i] >= maxN:
            maxN = numL[i]
            maxK = i
    for i in range(len(numL)):
        if numL[i] <= minN:
            minN = numL[i]
            minK = i
    for i in range(len(numL)):
        if secMax <= numL[i] <= maxN and i != maxK and i != minK:
            secMax = numL[i]
            secMaxK = i
    for i in range(len(numL)):
        if secMin >= numL[i] >= minN and i != minK and i != maxK:
            secMin = numL[i]
            secMinK = i
    for i in range(len(numL)):
        if thiMax <= numL[i] <= secMax <= maxN and i != maxK and\
                    i != secMaxK and i != minK and i != secMinK:
            thiMax = numL[i]
    if maxN * secMax * thiMax >= minN * secMin * maxN:
        print(maxN, secMax, thiMax)
    else:
        print(maxN, secMin, minN)
