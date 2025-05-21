N, C = list(map(int, input().replace(","," ").split()))
hist = []

for _ in range(N):
    s = input()
    if s == "halfplus":
        hist.append(1)
    else:
        hist.append(0)
hist = hist[::-1]
totalApples = 1
money = 0
for h in hist[1:]:
    totalApples *= 2
    if h == 1:
        totalApples += 1
print(totalApples*C - (C*(hist.count(1))//2))