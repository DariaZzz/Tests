inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
numR = [0] * 100
for line in lines:
    numR[int(line.split()[-2])] += 1
maxN = max(numR)
for i in range(len(numR)):
    if numR[i] == maxN:
        print(i, end=' ')
