for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    mn = min(A)
    mx = max(A)
    if mn == mx:
        c = A.count(mn)
        print(2*  ((c*(c-1))//2))
        continue
    mnCount = A.count(mn)
    mxCount = A.count(mx)
    print(2*mnCount*mxCount)