inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
k = int(lines.pop(0))
result = []
for line in lines:
    a = int(line.split()[-1])
    b = int(line.split()[-2])
    c = int(line.split()[-3])
    if a >= 40 and b >= 40 and c >= 40:
        result.append(a + b + c)
result.sort(reverse=True)
if len(result) <= k:
    print(0, file=outFile)
elif result[k - 1] == result[k]:
    if result[k - 1] == result[0]:
        print(1, file=outFile)
    else:
        for i in range(k - 2, -1, -1):
            if result[k - 1] != result[i]:
                print(result[i], file=outFile)
                break
else:
    print(result[k - 1])
