homes,guests=[],[]t a
for _ in range(int(input())):
    h,g = map(int, input().split())
    homes.append(h)
    guests.append(g)
tot = 0
for h in homes:
    for g in guests:
        if h == g:
            tot += 1
print(tot)

