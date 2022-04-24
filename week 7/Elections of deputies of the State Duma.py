inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
myDict = {}
myList1 = []
newDict = {}
sumN = 0
sumN1 = 0
for line in lines:
    a = int(line.split()[-1])
    line1 = ' '.join(line.split()[:-1])
    myDict[line1] = a
    sumN += a
firstElPri = sumN / 450
for line in myDict:
    myList1.append((line, float(myDict[line] % firstElPri), int(myDict[line] / firstElPri)))
    sumN1 += int(myDict[line] / firstElPri)
myList1.sort(key=lambda x: (-x[1], myDict[x[0]]))
for line in myList1:
    newDict[line[0]] = line[2]
while sumN1 < 450:
    for line in newDict:
        if sumN1 < 450:
            newDict[line] += 1
            sumN1 += 1
for line in myDict:
    print(line, newDict[line])
