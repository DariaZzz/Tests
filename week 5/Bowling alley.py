nAndK = list(map(int, input().split()))
numK = list(range(nAndK[0]))
numN = list(range(nAndK[1]))
for i in range(nAndK[1]):
    numN[i] = list(map(int, input().split()))
for i in range(len(numN)):
    for c in range(numN[i][0] - 1, numN[i][1]):
        numK[c] = '.'
for i in range(len(numK)):
    if numK[i] != '.':
        numK[i] = 'I'
print(*numK, sep='')
