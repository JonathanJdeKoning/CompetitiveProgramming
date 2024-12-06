N = int(input())
A = []
B = []
for _ in range(N):
    a,b = list(map(int, input().split()))
    A.append(a)
    B.append(b)
if A == sorted(A) and B == sorted(B):
    print("yes")
else:
    print("no")