from itertools import pairwise
N = int(input())
A = list(map(int, input().split()))
A.sort()
print(sum([(b-a)**2 for a,b in pairwise(A)]))