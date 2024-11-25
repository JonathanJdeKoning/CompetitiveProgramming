from collections import defaultdict
for _ in range(int(input())):
    N,L,F = list(map(int, input().split()))
    words = input().split()
    mp = defaultdict(int)

    for word in words:
        mp[word[-F:]] += 1
    
    ans = 0
    for val in mp.values():
        if val%2==1:
            ans += (val-1)//2
        else:
            ans += val//2
    print(ans)