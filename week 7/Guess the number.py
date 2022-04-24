inFile = open('input.txt')
n = int(inFile.readline())
lines = inFile.readlines()
mySet = set(range(1, n + 1))
newSet = set()
for line in lines:
    if line.strip() == 'YES' or line.strip() == 'NO' or line.strip() == 'HELP':
        if line.strip() == 'YES':
            mySet = mySet & newSet
        elif line.strip() == 'NO':
            mySet -= newSet
        newSet = set()
    else:
        for i in line.split():
            newSet.add(int(i))
print(*sorted(mySet))
