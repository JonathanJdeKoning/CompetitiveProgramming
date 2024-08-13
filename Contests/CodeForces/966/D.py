def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    s = input()

    ans = 0
    l = 0
    r = n-1
    pref = [0]
    tot =0 
    for num in nums:
        tot += num
        pref.append(tot)

    while l<r:
        if s[l] == "L" and s[r] == "R":
            ans += pref[r+1] - pref[l]
            l+=1
            r-=1
            continue
        elif s[l] == "L":
            r -= 1
        elif s[r] == "R":
            l += 1
        else:
            l+= 1
            r -= 1
    return ans





for _ in range(int(input())):
    print(solve())
