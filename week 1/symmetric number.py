number = int(input())
a = number // 1000
b = number // 100 % 10
c = number // 10 % 10
d = number % 10
print(0 ** (abs(a - d) + abs(b - c)))
