n,x = map(int, input().split())
ans = 0
curr = 1
for _ in range(n):
    l, r = map(int, input().split())
    
    while curr + x <= l:
        curr += x
    ans += (r-curr)+1
    curr = r+1
print(ans)
