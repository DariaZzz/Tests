n = int(input())
numL = list(map(int, input().split()))
numL.sort()
now = 101
k = 0
i = 0
c = 0
while i == 0 and c < len(numL):
    if numL[c] >= n:
        i = 1
        now = numL[c]
        k = 1
    c += 1
for i in range(len(numL)):
    if numL[i] - now >= 3:
        now = numL[i]
        k += 1
print(k)
