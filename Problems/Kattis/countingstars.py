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
case = 0
while True:
    case += 1
    try:
        R, C = map(int, input().split())
    except: break
    mat = [list(input().strip()) for _ in range(R)]

    dsu = DisjointSetUnion(R*C+1)
    evil = R*C
    for i, row in enumerate(mat):
        for j, cell in enumerate(row):
            
            uuid = i*C+j
            if cell == "#":
                dsu.union(uuid, evil)
            
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
    print(f"Case {case}: {len(dsu)-1}")




