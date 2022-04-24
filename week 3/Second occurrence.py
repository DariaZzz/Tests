a = input()
i = 0
s = 0
k = 2
kW = 0
now = 0
while i < k and a.find('f', s) != -1:
    f = a.find('f', kW)
    if f >= 0:
        i += 1
        kW = a.find('f', kW) + 1
        now = f
    s += 1
if now >= 0 and i == 2:
    print(now)
elif now >= 0 and i == 1:
    print(-1)
else:
    print(-2)
