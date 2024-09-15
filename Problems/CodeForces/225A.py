n = int(input())

top = int(input())
alt = 7-top

for _ in range(n):
    l,r = map(int, input().split())

    if l in (top,alt) or r in (top,alt):
        exit(print("NO"))

print("YES")

