from graphlib import* 
N,K=map(int, input().split())
e={i:[] for i in range(1,N+1)}
for _ in range(K):
    f,b=map(int, input().split())
    e[b].append(f)
print(*TopologicalSorter(e).static_order())