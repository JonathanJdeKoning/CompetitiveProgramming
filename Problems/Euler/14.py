def collatz(n):
    l =0 
    while n!= 1:
        l += 1
        if n%2==0:
            n//=2
        else:
            n = n*3+1
    return l+1

best = 0
ans = None
for i in range(2,1000001):
    if i%10000==0:
        print(i)
    c = collatz(i)
    if c > best:
        best = c
        ans = i

print(ans)

