for tc in range(int(input())):
    n, k = list(map(int, input().replace(","," ").split()))
    mul = n+1
    ans = 0
    cur = 1
    while(n >= k):
        if n&1: ans += cur
        n >>= 1
        cur <<=1
    print(mul*ans//2)