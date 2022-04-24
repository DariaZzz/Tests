nSec = int(input())
nHour = nSec // 3600 % 24
nMin = nSec // 60 % 60
nSec1 = nSec % 60
print(nHour, ':', nMin // 10, nMin % 10, ':', nSec1 // 10, nSec1 % 10, sep='')
