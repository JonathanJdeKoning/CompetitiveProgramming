N,M = list(map(int, input().split()))
cars = []
out = []
for _ in range(N):
    start, end = list(map(int, input().split()))
    cars.append((start, end))


for _ in range(M):
    x,y,t = list(map(int, input().split()))
    welp = 0
    for start, end in cars:
        back = 2*(end-start)
        left = t%back

        if left <= end - start:
            ans = start + left
        else:
            left -= (end-start)
            ans = end - left

        if ans >= x and ans <=y:
            welp += 1
    out.append(welp)

print("\n".join(map(str, out)))