def numN(a):
    i = 0
    for letter in a:
        if letter.isupper():
            i += 1
    return i


inFile = open('input.txt', 'r', encoding='utf8')
n = int(inFile.readline())
lines = inFile.readlines()
myDict = {}
numMist = 0
for line in lines:
    if len(line.split()) == 1:
        line1 = line.strip().lower()
        if line1 not in myDict:
            myDict[line1] = {line.strip()}
        else:
            myDict[line1].update({line.strip()})
    else:
        for word in line.split():
            if word.strip().lower() not in myDict\
                    and numN(word.strip()) != 1:
                numMist += 1
            elif word.strip().lower() in myDict and word.strip()\
                    not in myDict[word.strip().lower()]:
                numMist += 1
print(numMist)
