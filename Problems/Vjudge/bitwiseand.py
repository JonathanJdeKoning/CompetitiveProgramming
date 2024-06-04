for _ in range(int(input())):
    n,k = map(int, input().split())
    mx = 0
    for i in range(n+1):
        for j in range(n+1):
            if i>=j: continue
            x = j&i
            if x < k:
                mx = max(x, mx)
    print(mx)
