inFile = open('input.txt', 'r', encoding='utf8')
n = int(inFile.readline())
lines = inFile.readlines()
myDict = {}
myDict1 = {}
newDict = {}
myList = []
for line in lines:
    child = line.strip().split()[0]
    parent = line.strip().split()[1]
    myDict[child] = parent
for name in set(myDict.values()):
    if name not in myDict.keys():
        newDict[name] = 0
    else:
        if myDict[name] in newDict.keys():
            newDict[name] = 1 + newDict[myDict[name]]
for name in set(myDict.values()):
    if myDict[name] in newDict.keys():
        newDict[name] = 1 + newDict[myDict[name]]
print(newDict)
