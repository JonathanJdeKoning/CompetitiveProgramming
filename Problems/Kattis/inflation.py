from math import inf
def solve():
    n = int(input())
    canisters = sorted(list(map(int, input().split())), reverse=True)
    balloons = list(range(n,0,-1))
    mn = inf
    for i in range(n):
        balloon = balloons[i]
        can = canisters[i]
        
        if can > balloon: return "impossible"
        mn = min(mn,can/balloon)
    if mn.is_integer(): mn = int(mn)
    return mn



print(solve())
