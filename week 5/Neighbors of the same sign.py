numList = list(map(int, input().split()))
i = 1
len(numList)
while i < len(numList) and i != -1:
    if (numList[i] < 0 and numList[i - 1] < 0) or (numList[i] > 0 and
                                                   numList[i - 1] > 0) or\
            numList[i] == numList[i - 1] == 0:
        print(numList[i - 1], numList[i])
        i = -1
    else:
        i += 1
