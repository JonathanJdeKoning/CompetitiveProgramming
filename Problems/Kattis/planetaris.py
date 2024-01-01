systems, ships = list(map(int, input().split()))
battles = sorted(list(map(int, input().split())))

tot = 0
for battle in battles:
    if ships > battle:
        tot += 1
        ships-=(battle+1)
    else:
        break
print(tot)
