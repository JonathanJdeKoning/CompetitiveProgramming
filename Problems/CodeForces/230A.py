s, n = map(int, input().split())
drags = []
for _ in range(n):
    x,y = map(int, input().split())
    drags.append((x,y))

drags.sort()

for ds, up in drags:
    if s > ds:
        s += up
    else:
        exit(print("NO"))
print("YES")
