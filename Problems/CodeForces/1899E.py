for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mn = min(a)
    mindex = a.index(mn)
    if a[mindex+1:] != sorted(a[mindex+1:]):
        print(-1)
    else:
        print(mindex)

