n = int(input())
x = float(input())
n1 = float(input())
k = 0
sumN = n1 * x
while k < n - 1:
    n1 = float(input())
    sumN = (sumN + n1) * x
    k += 1
if n != 0:
    n1 = float(input())
    sumN += n1
    print(sumN)
else:
    print(n1)
