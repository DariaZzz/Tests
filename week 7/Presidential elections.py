inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
myDict = {}
for line in lines:
    myDict[line] = myDict.get(line, 0) + 1
sumN = 0
numR = []
for line in myDict:
    numR.append((myDict[line], line))
    sumN += int(myDict[line])
numR.sort(key=lambda x: -x[0])
if numR[0][0] / sumN > 0.5:
    print(numR[0][1], file=outFile)
else:
    print(numR[0][1], numR[1][1], sep='', end='', file=outFile)
