
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

n = int(input())
dsu = DisjointSetUnion(n+5)
m = int(input())
for i in range(1,n+1):
    row = input().split()
    for j, cell in enumerate(row, start=1):
        if cell=="1":
            dsu.union(i,j)

travel = list(map(int, input().split()))
base = dsu.find(travel[0])
for other in travel[1:]:
    if dsu.find(other) != base:
        exit(print("NO"))
print("YES")




