def tLag(n, k, num):
    if n > 0 and num > 0:
        if k ** 2 <= n and k > 0:
            tLag(n - k ** 2, k - 1, num - 1)
            print(k, end=' ')
        elif k ** 2 > n and k > 0:
            tLag(n, k - 1, num - 1)
        else:
            tLag(n - 1, k, num - 1)
            print(1, end=' ')
    if num <= 0 and n != 0:
        return ''


n1 = int(input())
k1 = n1 // 2
num1 = 4
print(tLag(n1, k1, num1))
