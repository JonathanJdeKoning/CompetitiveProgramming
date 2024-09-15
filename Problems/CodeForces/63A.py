n = int(input())
order = ["rat", "child", "man", "captain"]
a = []
for _ in range(n):
    name, pos = input().split()
    if pos == "woman": pos = "child"

    a.append((name, pos))

a.sort(key=lambda x: order.index(x[1]))

for x in a:
    print(x[0])
