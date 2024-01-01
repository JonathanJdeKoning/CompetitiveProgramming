import math
a,b,c,d = list(map(int, input().split()))

semiperimeter = (a + b + c + d) / 2
     
    # Applying Brahmagupta's formula to
    # get maximum area of quadrilateral
print(math.sqrt((semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c) * (semiperimeter - d)))