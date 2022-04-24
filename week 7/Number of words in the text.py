inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
mySet = set()
for line in lines:
    for j in line.strip().split():
        mySet.add(j)
print(mySet)
