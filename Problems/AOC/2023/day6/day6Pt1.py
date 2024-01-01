times = []
dists = []
with open("input.txt", "r") as file:
    lines = file.readlines()

    times = [int(x) for x in lines[0].split(":")[1].split()]
    dists = [int(x) for x in lines[1].split(":")[1].split()]
total = 1
for idx, time in enumerate(times):
    print(f"{time=}")
    counter = 1
    travel = 0

    while travel <= dists[idx]:
        print(f"{counter=}")
        travel = counter*(time-counter)
        counter += 1
        print(f"{travel=}")
    total*=(time+1)-((counter-1)*2)
print(total)

