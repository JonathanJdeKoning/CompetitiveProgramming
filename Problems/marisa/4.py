a,b,c = map(int, input().split())

if a <= b+c and b <= a+c and c <= b+a:
    print("YES")
else:
    print("NO")
