_, A2BTravelTime = list(map(int, input().replace(","," ").split()))
timeBetweenTrains, B2ATravelTime = list(map(int, input().replace(","," ").split()))

for i in range(5*60, 24*60, timeBetweenTrains):
    