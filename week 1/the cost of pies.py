nRub = int(input())
nPenny = int(input())
nPie = int(input())
totalCost = (nRub * 100 + nPenny) * nPie
print(totalCost // 100, totalCost % 100)
