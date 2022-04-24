numL = list(map(int, input().split()))
num = 1
now = numL[0]
for i in range(1, len(numL)):
    if numL[i] != numL[i - 1]:
        num += 1
        now = numL[i]
print(num)
