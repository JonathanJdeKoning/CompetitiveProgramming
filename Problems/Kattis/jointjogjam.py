import math
ksx, ksy, osx, osy, kex, key, oex, oey = list(map(int, input().split()))

sdist = math.sqrt((osx-ksx)**2+(osy-ksy)**2) 
edist = math.sqrt((oex-kex)**2+(oey-key)**2)
print(max(sdist, edist))
