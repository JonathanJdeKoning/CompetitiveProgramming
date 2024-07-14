def solve():
    n, k =map(int, input().split())
    sieve = [True]*(n+1)
    for i in range(2,n+1):
        if sieve[i]:
            for j in range(i,n+1,i):
                if sieve[j]:
                    sieve[j] = False
                    k -= 1
                    if k ==0: return j

print(solve())
