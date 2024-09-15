from collections import defaultdict
n,k = map(int, input().split())
want = list(map(int, input().split()))
child = defaultdict(list)

rest = set(range(1, (n*k)+1))
for i in range(len(want)):
    child[i].append(want[i])
    rest.discard(want[i])

l = len(rest)// k


for i in range(k):
    for _ in range(l):
        child[i].append(rest.pop())


for k,v in child.items():
    print(" ".join(map(str, v)))

