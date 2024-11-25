a,b,c = list(map(int, input().split()))
if c**2 == a**2 + b**2:
    print((a*b)//2)
else:
    print(-1)