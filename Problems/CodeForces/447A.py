p,n = map(int, input().split())
def h(x):
    return x%p

seen = set()

for i in range(1,n+1):
    num = int(input())
    res = h(num)
    if res in seen:
        exit(print(i))
    else:
        seen.add(res)
print(-1)
