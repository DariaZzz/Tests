inFile = open('input.txt')
lines = inFile.readlines()
myDict = {}
for line in lines:
    for word in line.split():
        word.strip()
        if word not in myDict:
            myDict[word] = 0
        else:
            myDict[word] += 1
        print(myDict[word], end=' ')
