a, b, c, d, e = int(input()), int(input()), int(input()),\
                int(input()), int(input())
sumN = 0
for i in range(1001):
    if i - e != 0 and\
            (a * i ** 3 + b * i ** 2 + c * i + d) / (i - e) == 0:
        sumN += 1
print(sumN)
