import math
n = float(input())
k = n - int(n)
if k // 0.5 == 1:
    print(math.ceil(n))
else:
    print(round(n))
