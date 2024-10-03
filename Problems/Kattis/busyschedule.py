order = ["12", "1", "2","3","4","5","6","7","8","9","10","11"]
while True:
    N = int(input())
    if N == 0: break
    times = []
    for _ in range(N):
        data = input().replace(":"," ").split()
        data[0] = int(data[0])
        data[1] = int(data[1])
        times.append(tuple(data))
    times.sort(key=lambda x: (x[-1], order.index(str(x[0])), x[1]))
    for time in times:
        print(f"{str(time[0])}:{str(time[1]).zfill(2)} {time[-1]}")
    print()
