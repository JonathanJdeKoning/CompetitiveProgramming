from math import gcd
def phi(n):
    count = 0

    for i in range(1,n+1):
        if gcd(i,n) == 1:
            count += 1
    return count

ans = [0]*1000001
for i in range(1,1001):
    p = phi(i)
    ans[i] = p

for i in range(1001):
    for j in range(1001):
        if i*j <=1000: continue
        if gcd(i,j) ==1:
            ans[i*j] = ans[i]*ans[j]

mx = 0
for i in range(1000001):
    if ans[i] ==0: continue
    val = i/ans[i]
    if val > mx:
        mx = val
        print(f"{i}: {val}")
