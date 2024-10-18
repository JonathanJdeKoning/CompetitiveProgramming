from math import ceil
for _ in range(int(input())):
    N,K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    if K == 1:
        print(A[ceil(N/2)-1])
    elif N == 1:
        print(sum(A))
    elif N == 2:
        print(sum(A[::2]))
    else:
        print(sum(A[K::(N-1)]))