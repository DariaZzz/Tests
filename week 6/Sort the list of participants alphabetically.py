fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
numL = []
for i in fin:
    numR = i.split(' ')
    numR.pop(2)
    numL.append(numR)
numL.sort()
for i in range(len(numL)):
    print(*numL[i], end='', file=fout)
fout.close()
