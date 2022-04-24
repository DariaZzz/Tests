a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
an1 = (a1 // a2) * (b1 // b2) * (c1 // c2)
an2 = (a1 // a2) * (b1 // c2) * (c1 // b2)
an3 = (a1 // b2) * (b1 // a2) * (c1 // c2)
an4 = (a1 // b2) * (b1 // c2) * (c1 // a2)
an5 = (a1 // c2) * (b1 // a2) * (c1 // b2)
an6 = (a1 // c2) * (b1 // b2) * (c1 // a2)
if an1 >= an2 and an1 >= an3 and an1 >= an4 and an1 >= an5 and an1 >= an6:
    print(an1)
elif an2 >= an1 and an2 >= an3 and an2 >= an4 and an2 >= an5 and an2 >= an6:
    print(an2)
elif an3 >= an1 and an3 >= an2 and an3 >= an4 and an3 >= an5 and an3 >= an6:
    print(an3)
elif an4 >= an1 and an4 >= an2 and an4 >= an3 and an4 >= an5 and an4 >= an6:
    print(an4)
elif an5 >= an1 and an5 >= an2 and an5 >= an3 and an5 >= an4 and an5 >= an6:
    print(an5)
else:
    print(an6)
