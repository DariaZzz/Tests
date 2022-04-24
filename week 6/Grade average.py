fin = open('input.txt', 'r', encoding='utf-8')
sum9 = 0
k9 = 0
sum10 = 0
k10 = 0
sum11 = 0
k11 = 0
for i in fin:
    numR = i.split(' ')
    if int(numR[2]) == 9:
        sum9 += int(numR[3])
        k9 += 1
    elif int(numR[2]) == 10:
        sum10 += int(numR[3])
        k10 += 1
    else:
        sum11 += int(numR[3])
        k11 += 1
if k9 == 0:
    print('0', end=' ')
else:
    print(sum9/k9, end=' ')
if k10 == 0:
    print('0', end=' ')
else:
    print(sum10 / k10, end=' ')
if k11 == 0:
    print('0', end=' ')
else:
    print(sum11/k11, end=' ')
