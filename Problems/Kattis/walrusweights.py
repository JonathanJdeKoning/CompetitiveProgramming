numplates = int(input())
plates = []
import math
mn = math.inf
for i in range(numplates):
    plates.append(int(input()))

for i in range(len(plates)):
    for j in range(len(plates)):
        if i==j: continue
        
        dist = abs(1000-(plates[i]+plates[j]))
        
        if dist < abs(mn-1000):
            mn = plates[i]+plates[j]
        elif dist == abs(mn-1000):
            mn = max(mn, plates[i]+plates[j])
print(mn)
