from collections import defaultdict
N = int(input())
names = defaultdict(int)

for _ in range(N):
    names[input()[0]] += 1

tri = lambda x: (x*(x-1))//2
ans = 0

for x in names.values():
    if x%2==0:
        ans += 2*tri(x//2)
    else:
        ans += tri(x//2)
        ans += tri(x//2+1)
print(ans)