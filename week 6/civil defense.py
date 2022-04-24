n = int(input())
numP = list(map(int, input().split()))
numP1 = []
for i in range(n):
    numP1.append((numP[i], i + 1))
numP1.sort()
# print(numP1)
n1 = int(input())
numB = list(map(int, input().split()))
numB1 = []
for i in range(n1):
    numB1.append((numB[i], i + 1))
numB1.sort()
# print(numB1)
numR = []
x = 0
for i in range(len(numP1)):
    for j in range(x, len(numB1)):
        if j != len(numB1) - 1:
            if abs(numP1[i][0] - numB1[j][0]) < abs(numP1[i][0] -
                                                    numB1[j + 1][0]):
                numR.append((numP1[i][1], numB1[j][1]))
                x = j
                break
        else:
            if abs(numP1[i][0] - numB1[j][0]) < abs(numP1[i][0] -
                                                    numB1[j - 1][0]):
                numR.append((numP1[i][1], numB1[j][1]))
            else:
                numR.append((numP1[i][1], numB1[j - 1][1]))
numR.sort()
for i in range(len(numR)):
    print(numR[i][1], end=' ')
