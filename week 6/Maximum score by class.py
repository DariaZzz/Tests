inFile = open('input.txt', 'r', encoding='utf-8')
lines = inFile.readlines()
numNew = [0] * 3
for line in lines:
    if int(line.split()[3]) > numNew[int(line.split()[2]) - 9]:
        numNew[int(line.split()[2]) - 9] = int(line.split()[3])
print(*numNew)
