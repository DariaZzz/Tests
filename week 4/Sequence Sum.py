def SecSum():
    n = int(input())
    if n != 0:
        return SecSum() + n
    return n


print(SecSum())
