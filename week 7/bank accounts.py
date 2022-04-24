def deposit(name, sumN):
    if name not in myDict:
        myDict[name] = sumN
    else:
        myDict[name] += sumN


def withdraw(name, sumN):
    if name not in myDict:
        myDict[name] = 0
        myDict[name] -= sumN
    else:
        myDict[name] -= sumN


def balance(name):
    if name not in myDict:
        print('ERROR')
    else:
        print(myDict[name])


def transfer(name1, name2, sumN):
    if name1 not in myDict:
        myDict[name1] = 0
    if name2 not in myDict:
        myDict[name2] = 0
    myDict[name1] -= sumN
    myDict[name2] += sumN


def income(p):
    for line in myDict:
        if myDict[line] > 0:
            myDict[line] += int(myDict[line] * p // 100)


inFile = open('input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
myDict = {}
for line in lines:
    line1 = line.strip().split()[0]
    name = line.strip().split()[1]
    if line1 == 'DEPOSIT':
        deposit(name, int(line.strip().split()[2]))
    elif line1 == 'WITHDRAW':
        withdraw(name, int(line.strip().split()[2]))
    elif line1 == 'BALANCE':
        balance(name)
    elif line1 == 'TRANSFER':
        transfer(name, line.strip().split()[2], int(line.strip().split()[3]))
    elif line1 == 'INCOME':
        income(int(line.strip().split()[1]))
