times = []
dists = []
with open("input.txt", "r") as file:
    lines = file.readlines()

    times = [int(x) for x in lines[0].split(":")[1].split()]
    dists = [int(x) for x in lines[1].split(":")[1].split()]
times = [int(str(times[0])+str(times[1]) + str(times[2])+str(times[3]))]
dists = [int(str(dists[0])+str(dists[1]) + str(dists[2])+str(dists[3]))]
print(times)
print(dists)
total = 1
for idx, time in enumerate(times):
    print(f"{time=}")
    counter = 1
    travel = 0

    while travel <= dists[idx]:
        travel = counter*(time-counter)
        counter += 1
    total*=(time+1)-((counter-1)*2)
print(total)

