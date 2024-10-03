N, K = list(map(int, input().split()))

peeps = []
for _ in range(N):
    start, stay = list(map(int, input().split()))
    end = start+stay+K
    peeps.append((start, end))

peeps.sort()

print(peeps)