n = int(input())
numN = list(map(int, input().split()))
k = int(input())
numK = list(map(int, input().split()))
for i in range(len(numK)):
    numN[numK[i] - 1] -= 1
for i in range(n):
    if numN[i] > -1:
        print('NO')
    else:
        print('YES')
