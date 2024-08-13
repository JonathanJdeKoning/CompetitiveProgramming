from math import factorial as f
def C(n,k):
    try:
        return f(n)// (f(n-k) * f(k))
    except:
        return -999

mod = 1e9+7
def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ones = a.count(1)
    zeros = a.count(0)
    poss = int(C(n,k)%mod)
    if zeros < (k//2)+1:
        bad = 0
    else:
        bad = k*int(C(zeros,(k//2)+1)%mod)
    print(f"###: {poss=}")
    print(f"###: {bad=}")
    return f"###: {poss-bad}"

for _ in range(int(input())):
    print(solve())
