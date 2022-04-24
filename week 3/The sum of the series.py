a = int(input())
k = 1
sum = 0
while k <= a:
    sum += 1 / k ** 2
    k += 1
print('{0:.5f}'.format(sum))
