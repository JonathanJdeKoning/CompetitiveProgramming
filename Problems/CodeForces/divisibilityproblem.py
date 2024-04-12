from math import ceil
for _ in range(int(input())):
    a,b=map(int,input().split())
    c = 0
    orig = b
    if a < b:
        print(b-a)
        continue
    m = ceil(a/b)
    b *=m
    print(b-a)
