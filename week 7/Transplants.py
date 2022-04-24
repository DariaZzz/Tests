numR = list(map(int, input().split()))
if numR[1] >= numR[0]:
    mySet = set(range(numR[0], numR[1] + 1))
else:
    mySet = set(range(numR[1], numR[0] + 1))
if numR[3] >= numR[2]:
    mySet1 = set(range(numR[2], numR[3] + 1))
else:
    mySet1 = set(range(numR[3], numR[2] + 1))
print(len(mySet & mySet1))
