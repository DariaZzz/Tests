def xor(x, y):
    if x == 1 and y == 0 or x == 0 and y == 1:
        return True
    return False


x1, y1 = int(input()), int(input())
print(int(xor(x1, y1)))
