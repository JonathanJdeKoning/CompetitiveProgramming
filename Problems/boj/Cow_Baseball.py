N = int(input())
A = sorted([int(input()) for _ in range(N)])
ans =0
for i in range(len(A)):
    for j in range(i+1,len(A)):
        for k in range(j+1,len(A)):
            d = A[j] - A[i]
            if d <= A[k] - A[j] <= 2*d:
                ans += 1

print(ans)