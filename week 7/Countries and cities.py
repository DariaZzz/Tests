inFile = open('input.txt')
myDict = {}
countries = int(inFile.readline())
lines = inFile.readlines()
cities = int(lines.pop(countries))
for line in range(countries):
    myList = lines[line].split()
    for city in myList[1:]:
        if myList[0] in myDict:
            myDict[myList[0]].add(city)
        else:
            myDict[myList[0]] = {city}
for city in lines:
    for country in myDict:
        if city.rstrip() in myDict[country]:
            print(country)
            break
