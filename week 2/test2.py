s1, f1, s2 = int(input()), int(input()), int(input())
f2, s3, f3 = int(input()), int(input()), int(input())
ans = 102
minAns = 101
s = 0
if f1 < s2 and f2 < s3 or f1 < s3 and f3 < s2:
    if s2 > f3:
        if abs(f1 - s1) >= abs(s2 - f3):
            ans = 1
        elif abs(f2 - s2) >= abs(s3 - f1):
            ans = 2
    elif s3 > f2:
        if abs(f1 - s1) >= abs(s3 - f2):
            ans = 1
        elif abs(f3 - s3) >= abs(s2 - f1):
            ans = 3
    if ans < minAns:
        minAns = ans
elif f2 < s1 and f1 < s3 or f2 < s3 and f3 < s1:
    if s1 > f3:
        if abs(f1 - s1) >= abs(s3 - f2):
            ans = 1
        elif abs(f2 - s2) >= abs(s1 - f3):
            ans = 2
    elif s3 > f1:
        if abs(f2 - s2) >= abs(s3 - f1):
            ans = 2
        elif abs(f3 - s3) >= abs(s1 - f2):
            ans = 3
    if ans < minAns:
        minAns = ans
elif f3 < s1 and f1 < s2 or f3 < s2 and f2 < s1:
    if s1 > f2:
        if abs(f1 - s1) >= abs(f2 - s3):
            ans = 1
        elif abs(f3 - s3) >= abs(s1 - f2):
            ans = 3
    elif s2 > f1:
        if abs(f2 - s2) >= abs(s1 - f3):
            ans = 2
        elif abs(f3 - s3) >= abs(s2 - f1):
            ans = 3
    if ans < minAns:
        minAns = ans
if minAns != 101:
    print(minAns)
    s += 1
if s == 0 and s1 <= s2 and s1 <= s3:
    if s1 <= f2 and s2 <= f1 and s2 <= f3 and s3 <= f2 or \
            s1 <= f3 and s3 <= f1 and s3 <= f2 and s2 <= f3:
        ans = 0
    elif s2 >= s3:
        if f3 >= s2:
            ans = 1
        elif f1 >= s3:
            ans = 2
    elif s3 >= s2:
        if f2 >= s3:
            ans = 1
        elif f1 >= s2:
            ans = 3
    if ans < minAns:
        minAns = ans
elif s2 <= s1 and s2 <= s3:
    if s2 <= f1 and s1 <= f2 and s1 <= f3 and s3 <= f1 or \
            s2 <= f3 and s3 <= f2 and s3 <= f1 and s1 <= f3:
        ans = 0
    elif s1 >= s3:
        if f2 >= s3:
            ans = 1
        elif f3 >= s1:
            ans = 2
    elif s3 >= s1:
        if f1 >= s3:
            ans = 2
        elif f2 >= s1:
            ans = 3
    if ans < minAns:
        minAns = ans
elif s3 <= s1 and s3 <= s2:
    if s3 <= f1 and s1 <= f3 and s1 <= f2 and s2 <= f1 or \
            s3 <= f2 and s2 <= f3 and s2 <= f1 and s1 <= f2:
        ans = 0
    elif s1 >= s2:
        if f3 >= s2:
            ans = 1
        elif f2 >= s1:
            ans = 3
    elif s2 >= s1:
        if f3 >= s1:
            ans = 2
        elif f1 >= s2:
            ans = 3
    if ans < minAns:
        minAns = ans
if minAns != 101 and s == 0:
    print(minAns)
elif s == 0:
    print(-1)
