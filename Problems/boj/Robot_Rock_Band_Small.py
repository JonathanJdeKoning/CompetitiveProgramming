for tc in range(int(input())):
    N,K = list(map(int, input().replace(","," ").split()))
    A = list(map(int, input().replace(","," ").split()))
    B = list(map(int, input().replace(","," ").split()))
    C = list(map(int, input().replace(","," ").split()))
    D = list(map(int, input().replace(","," ").split()))
    ans = 0
    for a in A:
        for b in B:
            for c in C:
                for d in D:
                    if a^b^c^d == K: ans += 1
    print(f"Case #{tc+1}: {ans}") 
    