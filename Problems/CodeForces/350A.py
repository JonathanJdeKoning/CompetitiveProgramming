right, wrong = map(int, input().split())

good = sorted(list(map(int, input().split())))
bad = sorted(list(map(int, input().split())))
for i in range(good[-1], bad[0]):
    if good[0]*2 <= i:
        exit(print(i))
print(-1)
