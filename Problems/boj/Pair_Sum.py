from collections import Counter
for tc in range(1, int(input())+1):
    N,M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    fq= Counter(A)
    ans = 0
    for num in A:
        inv = M-num
        ans += fq[inv]
    print(f"Case #{tc}: {ans//2}")