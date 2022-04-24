a = input()
k = a.find('f')
g = a.rfind('f')
l = k // g
print(str(k) * 0 ** (l * k == -1), " ", str(g) * 0 ** l, sep='')
