mx = -1
b = 0
for _ in range(int(input())):
    off, on = list(map(int, input().split()))
    b -= off
    mx = max(mx, b)
    b  += on
    mx = max(mx, b)

print(mx)