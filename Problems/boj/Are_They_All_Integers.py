N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if i == j: continue
        for k in range(N):
            if i == k or j == k: continue

            v = abs((A[i]-A[j]) / A[k])
            if not v.is_integer():
                exit(print("no"))
print("yes")
            