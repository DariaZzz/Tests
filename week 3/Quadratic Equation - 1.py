from math import sqrt
a = float(input())
b = float(input())
c = float(input())
if a != 0:
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (- b - sqrt(d)) / (2 * a)
        x2 = (- b + sqrt(d)) / (2 * a)
        if x1 < x2:
            print('{0:.6f}'.format(x1), '{0:.6f}'.format(x2))
        else:
            print('{0:.6f}'.format(x2), '{0:.6f}'.format(x1))
    elif d == 0:
        x = (- b) / (2 * a)
        print('{0:.6f}'.format(x))
