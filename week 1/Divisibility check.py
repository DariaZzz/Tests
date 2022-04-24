a = int(input())
b = int(input())
y = "YES" * 0 ** (a % b) + "NO" * (1 - 0 ** (a % b))
print(y)
