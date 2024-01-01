import math
while True:
    radius, marked, incircle = list(map(float, input().split()))

    if radius == 0: break

    true = math.pi*radius*radius

    est = (incircle / marked) * radius*2*radius

    print(f"{true} {est*2}")
