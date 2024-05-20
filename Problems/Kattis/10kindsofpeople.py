import sys
input = sys.stdin.readline
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

R, C = map(int, input().split())
mat = [list(input().strip()) for _ in range(R)]

dsu = DisjointSetUnion(R*C)
for i, row in enumerate(mat):
    for j, cell in enumerate(row):
        uuid = i*C+j

        try:
            next = mat[i][j+1]
            if next == cell:
                dsu.union(uuid, uuid+1)
        except:pass

        try:
            down = mat[i+1][j]
            if down == cell:
                dsu.union(uuid,uuid+C)
        except:pass
q = int(input())
for _ in range(q):
    x1,y1,x2,y2 = map(int, input().split())
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    if dsu.find(x1*C+y1) == dsu.find(x2*C+y2):
        if mat[x1][y1] == "0":
            print("binary")
        else:
            print("decimal")
    else:
        print("neither")



