inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
numR = [0] * 101
n9 = 0
n10 = 0
n11 = 0
for line in lines:
    if int(line.split()[-2]) == 9:
        numR[int(line.split()[-1])] += 1
for i in range(len(numR) - 1, -1, -1):
    if numR[i] != 0:
        n9 += 1
    if n9 == 2:
        print(i, end=' ')
        break
numR = [0] * 100
for line in lines:
    if int(line.split()[-2]) == 10:
        numR[int(line.split()[-1])] += 1
for i in range(len(numR) - 1, -1, -1):
    if numR[i] != 0:
        n10 += 1
    if n10 == 2:
        print(i, end=' ')
        break
numR = [0] * 100
for line in lines:
    if int(line.split()[-2]) == 11:
        numR[int(line.split()[-1])] += 1
for i in range(len(numR) - 1, -1, -1):
    if numR[i] != 0:
        n11 += 1
    if n11 == 2:
        print(i, end=' ')
        break
