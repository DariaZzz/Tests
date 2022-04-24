def add(a, b):
    if b > 0:
        return add(a + 1, b - 1)
    return a


a1 = int(input())
b1 = int(input())
print(add(a1, b1))
