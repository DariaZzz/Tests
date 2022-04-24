n = int(input())
# print(n[::-1])
k = 0
c = 0
i = 1
s = n
while s > 0:
    s = s // 10
    k += 1
print(k)
while i <= k:
    if i != 1:
        print((n % 10 ** i - n % 10 ** (i - 1)) // 10 ** (i - 1), end='')
    else:
        print(n % 10, end='')
    i += 1
