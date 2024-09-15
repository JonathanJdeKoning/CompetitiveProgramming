N = int(input())
A = list(map(int, input().split()))

mx = -1e18
for i in range(len(A)):
    for j in range(i+1,len(A)):
        mx = max(mx, A[i]*A[j])

print(mx)

