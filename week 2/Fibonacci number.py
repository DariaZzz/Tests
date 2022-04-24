n = int(input())
i = 2
now = 1
ans = 1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while i <= n:
        ans += now
        i += 1
        if ans == n:
            print(i)
            i = n + 1
        elif ans > n:
            print(-1)
            i = n + 1
        now = ans - now
