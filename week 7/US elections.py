inFile = open('input.txt')
lines = inFile.readlines()
myDict = {}
for line in lines:
    if line.split()[0] not in myDict:
        myDict[line.split()[0]] = int(line.split()[1])
    else:
        myDict[line.split()[0]] += int(line.split()[1])
for line in sorted(myDict):
    print(line, myDict[line])
