n,m = map(int, input().split())
n-=1
m-= 1
subs = (m*(m+1)*n*(n+1))//4

print(subs%(1e9+7))
