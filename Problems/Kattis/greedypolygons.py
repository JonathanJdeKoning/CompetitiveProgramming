from math import tan, pi

def cot(n):
    return 1/tan(n)
def ngonArea(sides, length):
    return sides*length**2*(1/4)*cot(pi/sides)
def sectorArea(angle, radius):
    return radius**2*angle*pi/360
def getAngle(sides):
    return 180 - ((sides-2)*180/sides)
for _ in range(int(input())):
    numSides, sideLength, expandDist, numGrabs = map(int, input().split())
    trueExpand = expandDist*numGrabs
    ans = ngonArea(numSides, sideLength)
    ans += numSides*(trueExpand*sideLength)

    ans += numSides*sectorArea(getAngle(numSides), trueExpand)



    print(ans)
