def clean(x):
    return x * x.isdecimal()


inFile = open('input.txt', 'r', encoding='utf8')
num = inFile.readline()
newnum = ''
for i in num:
    newnum += clean(i)
if len(newnum) > 10:
    newnum = newnum[1::]
elif len(newnum) < 8:
    newnum = '495' + newnum
lines = inFile.readlines()
for line in lines:
    newline = ''
    for i in line:
        newline += clean(i)
    if len(newline) > 10:
        newline = newline[1::]
    elif len(newline) < 8:
        newline = '495' + newline
    if newline == newnum:
        print('YES')
    else:
        print('NO')
