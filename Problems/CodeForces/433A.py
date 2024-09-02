n = int(input())
a = list(map(int, input().split()))
tot = sum(a)
goal = tot//2
if goal%100 != 0: exit(print("NO"))
if len(a) == a.count(200) and len(a)%2==1:
    exit(print("NO"))

print("YES")
