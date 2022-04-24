s1, f1, s2 = int(input()), int(input()), int(input())
f2, s3, f3 = int(input()), int(input()), int(input())
ans = 145
if f1 < s2 and f2 < s3 or f1 < s3 and f3 < s2:
    if s2 > f3:
        if f1 - s1 >= s2 - f3:
            ans = 1
        elif f2 - s2 >= s3 - f1:
            ans = 2
    elif s3 > f2:
        if f1 - s1 >= s3 - f2:
            ans = 1
        elif f3 - s3 >= s2 - f1:
            ans = 3
    print(ans)
else:
    print('wtf')