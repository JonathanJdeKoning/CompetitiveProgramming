for _ in range(int(input())):
    N = int(input())
    ans = 0
    while N:
        K = len(str(N))
        L = int(str(N)[0])
        R = L*(10**(K-1))
        N -= R
        ans += R
        N += R//10
    print(ans)