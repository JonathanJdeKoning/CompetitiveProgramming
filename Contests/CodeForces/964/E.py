def solve():
    l,r = map(int, input().split()) 
    ans = 0
    base = l+1
    for i in range(base,r+1):
        if i%3 == 0:
            base = i-1
            break

    windup = 0
    init = base
    while init != 0:
        windup += 1
        init//=3
    ans =2*windup

    for i in range(l, r+1):
        if i == base: continue
        
        num = i
        while num != 0:
            num//=3
            ans += 1
    return ans
    
for _ in range(int(input())):
    print(solve())
