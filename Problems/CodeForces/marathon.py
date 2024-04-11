for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    tot = len([x for x in [b,c,d] if x > a])
    print(tot)
