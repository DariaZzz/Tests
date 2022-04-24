inFile = open('input.txt')
myDict = {}

countrys = int(inFile.readline())
doc = inFile.readlines()
cities = int(doc.pop(countrys))

"""
Вариант оптимальной скорости кода
"""
for i in range(countrys):
    myList = doc[i].split()
    for city in myList[1:]:
        myDict[city] = myList[0]

for i in range(-cities, 0):
    city = doc[i].rstrip()
    print(myDict[city])

"""
Вариант верного верного словаря
"""
# for i in range(countrys):
#     myList = doc[i].split()
#     myDict[myList[0]] = set(myList[1:])
#
# # for i in range(countrys, cities + countrys):
#
# for i in range(-cities, 0):
#     doc[i].rstrip()
#     for key in myDict.keys():
#         if doc[i].rstrip() in myDict[key]:
#             print(key)

