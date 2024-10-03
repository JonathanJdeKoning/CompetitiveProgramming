from collections import Counter
N, K = map(int, input().split())
A = list(map(int, input().split()))

if K == 1:
    seen = set()
    for i, num in enumerate(A):
        inverse = 7777 - num
        if inverse in seen: exit(print("Yes"))
        seen.add(num)
    print("No")
if K == 2:
    if len(A) == len(set(A)):
        print("Unique")
    else:
        print("Contains duplicate")

if K == 3:
    fq = Counter(A)
    bestNum, bestCount = fq.most_common(1)[0]
    if bestCount > N/2: print(bestNum)
    else: print(-1)

if K ==4:
    A.sort()
    mid = N//2
    if N%2==1:
        print(A[mid])
    else:
        print(A[mid-1], A[mid])

if K == 5:
    print(" ".join(map(str, sorted([x for x in A if x >= 100 and x <= 999 ]))))
