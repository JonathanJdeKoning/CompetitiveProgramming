from itertools import dropwhile
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    A = list(dropwhile(lambda x: x==0, A))
    print(sum(A[:-1]) + A[:-1].count(0))
    