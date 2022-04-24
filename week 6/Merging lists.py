def merge(A, B):
    C = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if i == len(A) and j < len(B):
        for c in range(j, len(B)):
            C.append(B[c])
    elif i < len(A) and j == len(B):
        for c in range(i, len(A)):
            C.append(A[c])
    print(*C)


a = list(map(int, input().split()))
b = list(map(int, input().split()))
merge(a, b)
