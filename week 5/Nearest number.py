n = int(input())
numL = list(map(int, input().split()))
x = int(input())
nearN = numL[0]
dif = abs(x - numL[0])
for i in range(1, n):
    if abs(x - numL[i]) < dif:
        nearN = numL[i]
        dif = abs(x - numL[i])
print(nearN)
