s = list(map(int, input().split()))
numL = []
for i in range(s[1]):
    numL.append(int(input()))
numL.sort()
i = 0
k = 0
p = s[0]
while s[0] > 0 and i < len(numL):
    if p - numL[i] >= 0:
        p -= numL[i]
        k += 1
    i += 1
print(k)
