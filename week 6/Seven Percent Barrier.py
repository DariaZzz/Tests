inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
n1 = 0
numR = []
sumN = 0
for line in lines:
    if line == 'VOTES:\n':
        break
    elif line != 'PARTIES:\n':
        numR.append([0, line])
        n1 += 1
for line in lines:
    for i in range(n1):
        if numR[i][1] == str(line):
            numR[i][0] += 1
for i in range(len(numR)):
    numR[i][0] -= 1
    sumN += int(numR[i][0])
for i in range(len(numR)):
    if int(numR[i][0]) * 100 / sumN >= 7:
        print(numR[i][1], end='')
