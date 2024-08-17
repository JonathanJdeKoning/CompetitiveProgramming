n, d=map(int, input().split())
songs = list(map(int, input().split()))
perf = sum(songs) + 10*(len(songs)-1)
if perf > d:
    exit(print(-1))

print(2*(len(songs)-1)+(d-perf)//5)
