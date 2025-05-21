np = int(input())
nt = int(input())
probs = input().split()
a = [0]*np
for _ in range(nt):
    p = list(map(int, input().replace(","," ").split()))
    for i, c in enumerate(p):
        a[i] += c

mx = max(a)
i = a.index(mx)
print(probs[i])