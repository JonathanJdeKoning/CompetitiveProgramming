n,k = map(int, input().split())

a = []
curr = 0
for _ in range(n):
    l, r = map(int, input().split())
    curr += (r-l)+1

m = curr%k

if k-m == k:
    print(0)
else:
    print(k-m)
        
