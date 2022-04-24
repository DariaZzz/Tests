inFile = open('input.txt', 'r', encoding='utf8')
n = int(inFile.readline())
lines = inFile.readlines()
myDict = {}
for line in lines:
    if len(line.split()) > 1:
        line1 = line.strip().split()[0]
        line2 = line.strip().split()[1]
        myDict[line1] = line2
        myDict[line2] = line1
    else:
        print(myDict[line.strip()])
