N,X = map(int, input().split())
A = list(map(int, input().split()))
mp = {}
for i in range(N):
    num = A[i]
    inv = X- num
    if inv in mp:
        exit(print(i+1, mp[inv]+1))
    mp[num] = i
print("IMPOSSIBLE")