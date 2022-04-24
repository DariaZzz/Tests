n = int(input())
line = [[]] * n
for i in range(n):
    line[i] = list(map(str, input().split()))
line.sort(key=lambda x: int(x[1]), reverse=True)
for i in range(len(line)):
    print(line[i][0])
