k = int(input())
m = int(input())
n = int(input())
if k > 0 and m > 0 and n > 0:
    if n <= k:
        print(m * 2)
    elif n > k:
        ans = (n // k + 1 - 0 ** (n % k)) * m * 2
        print(ans)
else:
    print('0')
