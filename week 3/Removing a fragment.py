a = input()
h1 = a.find('h')
h2 = a.rfind('h') + 1
print(a[:h1], a[h2:], sep='')
