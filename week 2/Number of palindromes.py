k = int(input())
n = 1
ans = 0
while n <= k:
    i = 1
    coin = 0
    num = 0
    s = n
    while s > 0:
        s = s // 10
        num += 1
    s = num
    if n % 10 != 0:
        while i <= num // 2 <= s:
            if i != 1:
                a = (n % 10 ** i - n % 10 ** (i - 1)) // 10 ** (i - 1)
            else:
                a = n % 10
            b = (n % 10 ** s - n % 10 ** (s - 1)) // 10 ** (s - 1)
            if a == b:
                coin += 1
            i += 1
            s -= 1
        if coin == num // 2:
            ans += 1
    n += 1
print(ans)
