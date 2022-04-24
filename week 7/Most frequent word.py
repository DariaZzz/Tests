inFile = open('input.txt')
lines = inFile.readlines()
myDict = {}
for line in lines:
    for i in range(len(line.split())):
        if line.split()[i].strip() not in myDict:
            myDict[line.split()[i]] = 1
        else:
            myDict[line.split()[i]] += 1
maxN = -1
maxKey = ''
for line in sorted(myDict):
    if myDict[line] > maxN:
        maxN = myDict[line]
        maxKey = line
print(maxKey)
