wspeed = int(input())
roads = int(input())

for road in range(roads):
    name, rspeed = input().split()
    rspeed = int(rspeed)
    
    verdict = "lokud" if rspeed < wspeed else "opin"
    print(f"{name} {verdict}")