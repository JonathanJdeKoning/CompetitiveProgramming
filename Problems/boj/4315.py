from collections import defaultdict

while True:
    n = int(input())
    if n==0: break
    edges = defaultdict(list)
    marbles = defaultdict(int)
    ans = 0
    for _ in range(n):
        data = list(map(int,input().split()))
        node = data[0]
        edges[node] = data[3:]
        marbles[node] = data[1]

    def dfs(root):
        res = [dfs(child) for child in edges[root]]
        global ans
        ans += sum([abs(x) for x in res])
        return sum(res) + marbles[root] - 1

    dfs(1)
    print(ans)
