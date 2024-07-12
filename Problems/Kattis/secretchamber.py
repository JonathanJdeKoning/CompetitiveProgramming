class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

def f(c):
    return ord(c)-97

dsu = DisjointSetUnion(27)
numTrans, numPairs = map(int, input().split())
for _ in range(numTrans):
    a, b = map(f,input().split())
    dsu.union(a,b)
for _ in range(numPairs):
    a,b = input().split()
    a = [f(x) for x in a]
    b = [f(x) for x in b]
    if len(a) != len(b): print("no");break

    for c,d in zip(a,b):
        if dsu.find(c) != dsu.find(d):
            print("no")
            break
    else:
        print("yes")

