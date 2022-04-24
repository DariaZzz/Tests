mySet = set(map(int, input().split()))
mySet2 = set(map(int, input().split()))
print(*sorted(list(mySet & mySet2)))
