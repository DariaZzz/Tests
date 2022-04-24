inFile = open('input.txt', 'r', encoding='utf8')
n = int(inFile.readline())
mySet = set(range(1, n + 1))
lines = inFile.readlines()
for line in lines:
    if line.strip() == 'HELP':
        print(*sorted(mySet))
        break
    line1 = set(map(int, line.split()))
    intersection = mySet.intersection(line1)
    if len(intersection) > len(mySet) // 2:
        print('YES')
        mySet = intersection
    else:
        print('NO')
        mySet -= intersection
