a = int(input())
b = int(input())
c = abs(a - b)
a = a + c * 0 ** ((a + 1) // (b + 1))
print(a)
