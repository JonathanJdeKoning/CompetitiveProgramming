from collections import Counter, deque, defaultdict, deque
from itertools import pairwise, groupby
from functools import reduce, cache
from math import ceil, floor, sqrt, gcd

factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def solve():
    N = int(input())
    A = list(map(int, input().replace(","," ").split()))
    factfq = Counter()

    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            a = A[i]
            b = A[j]

            if gcd(a,b) == 2 or gcd(a, b) == 1:
                return "Yes"
    return "No"

for tc in range(int(input())):
    print(solve())