N = int(input())

for tc in range(N):
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, 13):
        for j in range(i+1, 13):
            ck = A[i:j]
            if min(ck) > A[i-1] and min(ck) > A[j]:
                ans += 1
                #print(ck)
    print(tc+1, ans) 