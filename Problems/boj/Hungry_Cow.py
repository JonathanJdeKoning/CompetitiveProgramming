N, T = list(map(int, input().replace(","," ").split()))
eated = 0
tot = 0
curr = 1
for _ in range(N):
    day, bales = list(map(int, input().replace(","," ").split()))
    length = day - curr
    
