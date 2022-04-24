def fact(a, acc=1):
    if a > 1:
        return fact(a - 1, acc * a)
    return acc


def C(n, k):
    return int(fact(n) / (fact(n - k) * fact(k)))


n1, k1 = int(input()), int(input())
print(C(n1, k1))
