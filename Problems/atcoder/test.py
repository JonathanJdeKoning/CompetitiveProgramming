for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input().lstrip("0").rstrip("1"))
    ones = s.count("1")
    if ones <= k or len(s)-ones <= k:
        print(0); continue
    
    impact = []
    currimp = 0
    for i, c in enumerate(s):
        if c == "1":
            currimp += 1
        else:
            impact.append((currimp, i))
            
    currimp = 0
    for i, c in enumerate(s[::-1]):
        if c == "0":
            currimp += 1
        else:
            impact.append((currimp, (n-i)-1))
            
    impact.sort(reverse=True)
    for imp, idx in impact[:k]:
        s[idx] = str(int(s[idx])^1)
        
    total = 0
    ones = 0
    for c in s:
        if c == "1":
            ones += 1
        else:
            total += ones
    print(total)
    
    
