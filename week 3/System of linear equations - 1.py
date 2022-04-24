a, b, c, d, e, f = float(input()), float(input()), float(input()),\
                   float(input()), float(input()), float(input())
a1 = a - c
b1 = b - d
e1 = e - f
if b1 != 0 and (a * b1 - b * a1) != 0:
    x = (e * b1 - b * e1) / (a * b1 - b * a1)
    y = (e1 - a1 * x) / b1
print('{0:.6f}'.format(x), '{0:.6f}'.format(y))
