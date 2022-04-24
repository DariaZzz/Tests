numR = list(map(int, input().split()))
mySet = set(numR)
for i in range(len(numR)):
    if numR[i] in mySet:
        print('NO')
        mySet.remove(numR[i])
    else:
        print('YES')
