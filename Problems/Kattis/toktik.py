from collections import defaultdict

d = defaultdict(int)
for _ in range(int(input())):
    name, money = input().split()
    d[name] += int(money)
print(sorted(d.items(), key=lambda x:x[1])[-1][0])
