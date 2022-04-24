s1, f1, s2 = int(input()), int(input()), int(input())
f2, s3, f3 = int(input()), int(input()), int(input())
s = 0
if (s1 <= f2 and s2 <= f1 and s2 <= f3 and s3 <= f2) or\
    (s1 <= f3 and s3 <= f1 and s3 <= f2 and s2 <= f3) or \
    (s2 <= f1 and s1 <= f2 and s1 <= f3 and s3 <= f1) or \
    (s2 <= f3 and s3 <= f2 and s3 <= f1 and s1 <= f3) or\
    (s3 <= f1 and s1 <= f3 and s1 <= f2 and s2 <= f1) or\
        (s3 <= f2 and s2 <= f3 and s2 <= f1 and s1 <= f2):
    print(0)
    s1 = s2 = s3 = f1 = f2 = f3 = 0
elif s1 <= s2 and s1 <= s3:
    if f3 >= s2 >= s3:
        print(1)
        s += 1
    elif f1 >= s3 and s2 >= s3:
        print(2)
        s += 1
    elif f2 >= s3 >= s2:
        print(1)
        s += 1
    elif f1 >= s2 and s3 >= s2:
        print(3)
        s += 1
elif s2 <= s1 and s2 <= s3:
    if s1 >= s3 and f2 >= s3:
        print(1)
        s += 1
    elif f3 >= s1 >= s3:
        print(2)
        s += 1
    elif f1 >= s3 >= s1:
        print(2)
        s += 1
    elif f2 >= s1 and s3 >= s1:
        print(3)
        s += 1
elif s3 <= s1 and s3 <= s2:
    if s1 >= s2 and f3 >= s2:
        print(1)
        s += 1
    elif f2 >= s1 >= s2:
        print(3)
        s += 1
    elif s2 >= s1 and f3 >= s1:
        print(2)
        s += 1
    elif f1 >= s2 >= s1:
        print(3)
        s += 1
if s == 0 and (f1 < s2 and f2 < s3) or (f1 < s3 and f3 < s2):
    if s2 > f3:
        if f1 - s1 >= s2 - f3:
            print(1)
        elif f2 - s2 >= s3 - f1:
            print(2)
    elif s3 > f2:
        if f1 - s1 >= s3 - f2:
            print(1)
        elif f3 - s3 >= s2 - f1:
            print(3)
elif (f2 < s1 and f1 < s3) or (f2 < s3 and f3 < s1):
    if s1 > f3:
        if f1 - s1 >= s3 - f2:
            print(1)
        elif f2 - s2 >= s1 - f3:
            print(2)
    elif s3 > f1:
        if f2 - s2 >= s3 - f1:
            print(2)
        elif f3 - s3 >= s1 - f2:
            print(3)
elif f3 < s1 and f1 < s2 or f3 < s2 and f2 < s1:
    if s1 > f2:
        if f1 - s1 >= f2 - s3:
            print(1)
        elif f3 - s3 >= s1 - f2:
            print(3)
    elif s2 > f1:
        if f2 - s2 >= s1 - f3:
            print(2)
        elif f3 - s3 >= s2 - f1:
            print(3)
elif s1 + s2 + s3 + f1 + f2 + f3 != 0:
    print(-1)
