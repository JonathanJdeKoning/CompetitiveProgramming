T = int(input())
for _ in range(T):
    d = {} 
    N = int(input())
    A = input().split()
    for num in A:
        d[num] = d.get(num,0)+1
    mx = max(d.values())
    o = mx

    ans = 0
    while mx < N:
        ans += 1
        mx*=2
    print(ans + N-o)
        

