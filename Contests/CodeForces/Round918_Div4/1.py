tc = int(input())
for _ in range(tc):
    a,b,c = list(map(int, input().split()))
    if a==b:
        print(c)
    elif b==c:
        print(a)
    elif c==a:
        print(b)
