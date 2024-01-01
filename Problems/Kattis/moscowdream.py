a,b,c,n = list(map(int, input().split()))

if sum([a,b,c]) < n or a < 1 or b < 1 or c < 1 or n <3:
    print("NO")
else: print("YES")
