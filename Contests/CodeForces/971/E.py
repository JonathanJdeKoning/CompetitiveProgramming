from math import inf
def f(start, end):
    n = 1+(end-start)
    return n*(start+end)//2



def solve():
    n,k = map(int, input().split())
    
    left = k
    right = n+k 
    mn = inf

    while (right-left) >= 3:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        f1 = abs(f(k,mid1)-f(mid1+1,n+k)) 
        f2 = abs(f(k,mid2) -f(mid2+1,n+k))
        if f1 > f2:
            left = mid1
            mn = min(mn, f2)
        else:
            right = mid2
            mn = min(mn, f2)
    mn = min(mn, abs(f(k,left) - f(left+1, n+k)), abs(f(k,left+1) - f(left+2, n+k)), abs(f(k,right) - f(right+1, n+k)))
    return mn





for _ in range(int(input())):
    print(solve())
