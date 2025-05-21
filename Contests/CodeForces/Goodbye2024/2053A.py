
from itertools import pairwise



def solve():
    N = int(input())
    A = list(map(int, input().replace(","," ").split()))
    for i,j in pairwise(A):
        poss = [[i,i,i], [i,i,j], [i,j,j,], [j,j,j]]
        for a,b,c in poss:
            if not (a+b > c and a+c > b and b+c > a):
                break
        else:
            return "YES"
    return "NO"

for tc in range(int(input())):
    print(solve())