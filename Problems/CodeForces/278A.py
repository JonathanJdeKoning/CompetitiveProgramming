n = int(input())

a = list(map(int, input().split()))
s,t = map(int, input().split())
s,t = min(s,t), max(s,t)

print(min(sum(a[s-1:t-1]), sum(a[:s-1])+sum(a[t-1:])))

