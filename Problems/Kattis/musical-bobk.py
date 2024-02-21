#!/usr/bin/python3

(c, n) = map(int, input().split(' '))
times = list(map(int, input().split(' ')))

size = ((c + 1) * (c + 2)) // 2
table = [[False] * size, [False] * size]
table[0][0] = True
table[1][0] = True
src = 0
dest = 1

for i in range(n):
    c1 = 0
    c2 = 0
    for j in range(size):
        if table[src][j]:
            # we can choose to not use song i
            table[dest][j] = True
            # if song i fits, we can add to cd 1
            if c1 + times[i] <= c:
                table[dest][((c1 + times[i]) * (c1 + times[i] + 1)) // 2 + c2] = True
            # same with cd 2
            if c2 + times[i] <= c:
                a = c1
                b = c2 + times[i]
                if a < b:
                    (a, b) = (b, a)
                table[dest][(a * (a + 1)) // 2 + b] = True

        # move c1 and c2
        c2 += 1
        if c2 > c1:
            c2 = 0
            c1 += 1

    # swap src and dest roles
    (dest, src) = (src, dest)

c1 = 0
c2 = 0
best = [0, 0]
for i in range(size):
    if table[src][i] and (c1 + c2 > best[0] + best[1] or (c1 + c2 == best[0] + best[1] and abs(c1-c2) < abs(best[0]-best[1]))):
        best = [c1, c2]

    c2 += 1
    if c2 > c1:
        c2 = 0
        c1 += 1

if best[0] < best[1]:
    (best[0], best[1]) = (best[1], best[0])

print(best[0], best[1])
