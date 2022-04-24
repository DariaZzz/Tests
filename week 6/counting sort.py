def CountSort(a):
    numNew = [0] * 101
    for i in range(len(a)):
        numNew[a[i]] += 1
    for i in range(len(numNew)):
        print((str(i) + ' ') * numNew[i], end='')


numL = list(map(int, input().split()))
CountSort(numL)
