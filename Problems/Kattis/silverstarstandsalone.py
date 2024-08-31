def is_prime(n):
    if n < 2: 
         return False;
    if n % 2 == 0:             
         return n == 2
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True
star = int(input())
stars = []
for i in range(2, star+1):
    if is_prime(i): stars.append(i)

dp = [0]*len(stars)
dp[0] = 1

for i, num in enumerate(stars[1:], start=1):
    ans = 0
    curr = i-1
    for j in range(num-1, num-15, -1):
        if j < 0: break
        if is_prime(j):
            ans += dp[curr]
            curr -= 1
    dp[i] = ans

print(dp[-1])
