for tc in range(int(input())):
    N = int(input())
    A = list(map(int, input().replace(","," ").split()))
    neg = A.count(-1)
    pos = A.count(1)
    par = neg%2
    cum = sum(A)
    ans = 0
    while cum < 0 or par == 1:
        cum += 2
        par = abs(par-1)
        ans += 1
    print(ans)
