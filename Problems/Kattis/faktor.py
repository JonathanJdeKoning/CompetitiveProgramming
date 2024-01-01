import math

topub, impact = list(map(int, input().split()))

res = 0
count = 0

while res < impact:
    
    res = math.ceil(count / topub)
    count += 1
print(int(count)-1)