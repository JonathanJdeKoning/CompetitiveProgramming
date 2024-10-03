N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 1: print(7)

if K == 2:
    if A[0] > A[1]: print("Bigger")
    elif A[0] < A[1]: print("Smaller")
    else: print("Equal")

if K == 3:print(sorted(A[:3])[1])
if K == 4: print(sum(A))
if K == 5: print(sum([x for x in A if x%2==0]))
if K ==6:print("".join(map(lambda x: chr((x%26)+97), A)))
if K ==7:
    seen = set([0])
    curr = 0
    while True:
        curr = A[curr]
        if curr < 0 or curr > len(A)-1:
            exit(print("Out"))
        if curr in seen: exit(print("Cyclic"))
        seen.add(curr)
        if curr == len(A)-1: exit(print("Done"))





