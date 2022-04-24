percent = int(input())
rub = int(input())
pen = int(input())
allPen = rub * 100 + pen
ans = allPen + percent / 100 * allPen
print(int(ans // 100), int(ans % 100))
