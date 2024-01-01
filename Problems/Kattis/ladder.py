import math
height, degrees = list(map(int, input().split()))
leg = height*math.tan(math.radians(90-degrees))
length = math.sqrt(leg**2+height**2)
print(int(math.ceil(length)))
