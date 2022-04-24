n = int(input())
i = 3
now = 1
ans = 1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while i <= n:
        ans += now
        now = ans - now
        i += 1
    print(ans)
