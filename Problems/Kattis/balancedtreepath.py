from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
n = int(input())
s = "#"+input()
good = {")": "(", "]":"[","}":"{"}
close = {")","]","}"}
edges = defaultdict(list)
seen = set()
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
total = 0
vals = []
def dfs(node, seen):
    global total
    global vals

    if node in seen:
        return
    
    seen.add(node)
    val = s[node]
    print(f"{node}|{val}: {vals}")
    if val in close:
        if not vals: return
        prev = vals.pop()
        if prev == good[val]:
            if not vals: total += 1
        else:
            return
    else:
        vals.append(val)


    for edge in edges[node]:
        if edge not in seen:
            dfs(edge, seen)   
    
    if vals:
        vals.pop()
   

for i in range(1,n+1):
    vals = []
    dfs(i, set())
    
print(total)

