numL = list(map(int, input().split()))
sumK = 0
for i in range(len(numL)):
    print(str(numL[i]) * 0 ** (numL.count(numL[i]) - 1),
          end=' ' * 0 ** (numL.count(numL[i]) - 1))
    sumK = 0
