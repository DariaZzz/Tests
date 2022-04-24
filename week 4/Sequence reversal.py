def SecTurn():
    n = int(input())
    if n != 0:
        SecTurn()
    print(n)


SecTurn()
