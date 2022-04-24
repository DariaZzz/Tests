inFile = open('input.txt')
lines = inFile.readlines()
myDict = {}
for line in lines:
    name = line.split()[0].strip()
    thing = line.split()[1].strip()
    number = line.split()[2].strip()
    if name not in myDict:
        myDict[name] = {thing: number}
    elif thing not in myDict[name]:
        myDict[name].update({thing: int(number)})
    else:
        myDict[name].update({thing: int(myDict[name][thing]) + int(number)})
for line in sorted(myDict):
    print(line, ':', sep='')
    for line1 in sorted(myDict[line]):
        print(line1, myDict[line][line1])
