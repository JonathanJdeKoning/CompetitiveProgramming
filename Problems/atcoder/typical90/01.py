from itertools import pairwise
N, L = list(map(int, input().replace(","," ").split()))
K = int(input())
A = list(map(int, input().replace(","," ").split()))
gaps = [b-a for a,b in pairwise(A)]

def condition(mid):
    if mid < max(gaps): return False
    
    cuts = K
    prevCut = 0
    currLen = 0
    for i, currCut in enumerate(A):
        possLen = (currCut - prevCut)
        if possLen <= mid:
            continue
        else:
            cuts -= 1
            prevCut = A[i-1]
            currLen = (currCut - prevCut)
            if cuts == 0:
                ribbonLeft = L - A[i-1]
                break
    return cuts or ribbonLeft <= mid
    


low = 1
high = L
while low < high:
    mid = (low + high)//2

    if condition(mid):
        high = mid
    else:
        low = mid + 1
print(low)