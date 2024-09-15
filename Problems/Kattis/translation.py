n = int(input())
s = input().split()
m = int(input())
d = {}
for _ in range(m):
    a,b = input().split()
    d[a]=b

print(" ".join(map(lambda x:d[x], s)))
