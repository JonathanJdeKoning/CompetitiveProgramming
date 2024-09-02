n,k = map(int, input().split())

a = list(map(int, input().split()))
l = 0
r = k-1
curr = sum(a[l:r+1])
ans = 1
mn = curr

while True:
    curr -= a[l]
    l += 1
    r += 1
    if r  == len(a): break
    curr += a[r]

    if curr < mn:
        mn = curr
        ans = l+1

print(ans)    


