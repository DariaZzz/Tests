inFile = open('input.txt', 'r', encoding='utf8')
numR = tuple(map(int, inFile.readline().split()))
lines = inFile.readlines()
mySet = set()
saturdays = set(range(6, numR[0] + 1, 7))
sundays = set(range(7, numR[0] + 1, 7))
for line in lines:
    now, add1 = map(int, line.split())
    bast = range(now, numR[0] + 1, add1)
    mySet.update(bast)
print(len(mySet - saturdays - sundays))
