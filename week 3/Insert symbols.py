a = input()
f = a.count('')
if len(a) >= 2:
    print(a[0] + a[1:len(a) - 1].replace('', '*') + a[len(a) - 1])
else:
    print(a)
