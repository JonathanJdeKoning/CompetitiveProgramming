N,M = list(map(int, input().split()))
a = 0
b = 0
for _ in range(N):
    i,j = list(map(int, input().split()))
    a += i*j
for _ in range(M):
    i,j = list(map(int, input().split()))
    b += i*j

if a == b:
    print("same")
else:
    print("different")
