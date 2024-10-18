from collections import Counter
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    fq = Counter(A)
    if any(list(filter(lambda x:x%2==1, fq.values()))):
        print("YES")
    else:
        print("NO")
