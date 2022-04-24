def Intersection(A, B):
    C = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            C.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(*C)


a = list(map(int, input().split()))
b = list(map(int, input().split()))
Intersection(a, b)
