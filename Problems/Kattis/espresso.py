orders, tank = list(map(int, input().split()))
currtank = tank
refills = 0
for _ in range(orders):
    order = input()

    needed = int(order[0])
    if "L" in order:
        needed += 1

    if needed > currtank:
        currtank = tank
        refills += 1

    currtank -= needed
print(refills)
    

