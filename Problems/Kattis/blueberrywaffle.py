rate, time = list(map(int, input().split()))

rotations = round(time/rate)

print("up") if rotations%2 == 0 else print("down")
