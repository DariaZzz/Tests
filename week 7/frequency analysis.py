inFile = open('input.txt')
lines = inFile.readlines()
myDict = {}
for line in lines:
    for i in range(len(line.split())):
        if line.split()[i].strip() not in myDict:
            myDict[line.split()[i]] = 1
        else:
            myDict[line.split()[i]] += 1
numR = []
for line in myDict:
    numR.append((myDict[line], line))
numR.sort(key=lambda x: (-x[0], x[1]))
for line in numR:
    print(line[1])
