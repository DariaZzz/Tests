a = input()
h1 = a.find('h')
h2 = a.rfind('h')
print(a[:h1 + 1] + a[(h1 + 1):h2].replace('h', 'H') + a[h2:])
