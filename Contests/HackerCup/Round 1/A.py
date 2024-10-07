for tc in range(1, int(input())+1):
    N = int(input())
    stations = []
    for _ in range(N):
        start, end = list(map(int, input().split()))
        stations.append((start, end))
    
    low = 0
    high = len(stations)*2
    good = False
    while abs(low - high) > 0.00000001:
        #print(f"L: {low}, H: {high}")
        speed = (low + high)/2
        #print(f"{speed=}")
        for miles, (start, end) in enumerate(stations, start=1):
            currtime = miles/speed
            #print(f"{currtime=}")
            if currtime > end:
                #print("Greater")
                low = speed
                break
            elif currtime < start:
                #print("Lower")
                high = speed
                break
        else:
            good = True
            high = speed
            

    if good:
        print(f"Case #{tc}: {'{:.10f}'.format(round(low,10))}")
    else:
        print(f"Case #{tc}: {-1}")