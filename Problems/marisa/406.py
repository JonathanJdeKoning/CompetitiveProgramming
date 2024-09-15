N = int(input())
A = list(map(int, input().split()))

mx = max(A)
idx = A.index(mx)
print(mx, idx+1)
