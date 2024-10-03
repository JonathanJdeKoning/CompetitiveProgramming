n = int(input())
A = [int(input()) for _ in range(n)]

mx = max(A)

if A[0] == mx: print("S")
else: print("N")