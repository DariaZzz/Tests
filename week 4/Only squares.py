from math import sqrt


def onlyS(n1=0):
    n = int(input())
    if n != 0:
        if n > 0 and sqrt(n) - int(sqrt(n)) == 0:
            onlyS(n1 + 1)
            print(n, end=' ')
            if n1 != 0:
                return n1
            else:
                return ''
        else:
            onlyS(n1)
            if n1 != 0:
                return n1
            else:
                return ''
    if n1 == 0:
        return 0
    else:
        return ''


print(onlyS())
