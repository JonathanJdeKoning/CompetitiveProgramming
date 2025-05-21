from math import gcd
def solve():
    N = int(input())
    A = list(map(int, input().replace(","," ").split()))
    if len(set(A)) == 1: return "YES"
    if A == sorted(A): return "YES"

    for i in range(len(A) - 2):
        if A[i+2]%A[i] == 0 and A[i+1] < A[i]:
            return "NO"
    return "YES"
    
for tc in range(int(input())):
    print(solve())