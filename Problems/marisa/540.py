from itertools import pairwise
N = int(input())
A = list(map(int, input().split()))
print(max([abs(b-a) for a,b in pairwise(A)]))
