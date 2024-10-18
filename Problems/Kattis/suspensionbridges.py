from math import sinh, cosh
dist, want = list(map(int, input().split()))
if dist == 0 : exit(print(want))
if want == 0: exit(print(dist))
def length(a):
    return 2*a*sinh(dist/(2*a))

def sag(a):
    return a*cosh(dist/(2*a))

low = 0
high = want*5000

while (high-low) > 0.0000000001:
    mid = (low+high)/2
    #print(mid, sag(mid))
    if sag(mid) < mid+want:
        high=mid
    else:
        low=mid

print(length(low))
