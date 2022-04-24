a, b, c, d, e, f = float(input()), float(input()), float(input()),\
                   float(input()), float(input()), float(input())
a1 = a - c
b1 = b - d
e1 = e - f
if a1 == 0 and b1 == 0 and e1 == 0:
    print(5)
elif e1 == 0 and a1 == 0 and a * b1 - b * a1 != 0 and b1 != 0:
    x = (e * b1 - b * e1) / (a * b1 - b * a1)
    y = (e1 - a1 * x) / b1
    print('3', '{0:.6f}'.format(y))
elif e1 == 0 and b1 == 0 and b * a1 - a * b1 != 0 and a1 != 0:
    y = (a1 * e - a * e1) / (b * a1 - a * b1)
    x = (e1 - b1 * y) / a1
    print('4', '{0:.6f}'.format(x))
elif a * b1 - b * a1 == 0 and b1 == 0 or b * a1 - a * b1 == 0 and a1 == 0:
    print(0)
else:
    x = (e * b1 - b * e1) / (a * b1 - b * a1)
    y = (e1 - a1 * x) / b1
