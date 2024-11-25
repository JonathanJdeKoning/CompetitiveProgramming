snow = 0
for _ in range(int(input())):
    op, n = list(map(int, input().split()))
    if op == 0:
        snow += n
    else:
        snow -= n
        if snow < 0:
            snow = 0
print(snow)