percent = int(input())
rub = int(input())
pen = int(input())
k = int(input())
i = 1
ans = 0
while i <= k:
    allPen = rub * 100 + pen
    ans = allPen + percent / 100 * allPen
    ans1 = int(ans // 100)
    rub = ans1
    pen = int(ans % 100)
    i += 1
print(rub, pen)
