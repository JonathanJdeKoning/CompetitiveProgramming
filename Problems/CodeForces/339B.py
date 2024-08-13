n,m = map(int, input().split())
curr = 1
ans = 0
need = list(map(int, input().split()))
for task in need:
    ans += (task-curr)%n
    curr = task

print(ans)
