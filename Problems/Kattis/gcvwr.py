gcvwr, truckWeight, numItems = list(map(int, input().split()))

items = list(map(int, input().split()))
left = gcvwr - truckWeight

left = left*0.9

for item in items:
    left -= item

print(int(left))