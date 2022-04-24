def IsAscending(numList):
    isT = 1
    i = 1
    while isT == 1 and i < len(numList):
        if numList[i] > numList[i - 1]:
            isT = 1
        else:
            isT = 0
        i += 1
    return isT


numList1 = list(map(int, input().split()))
if IsAscending(numList1) == 1:
    print('YES')
else:
    print('NO')
