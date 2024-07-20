prevSun, sunCyc = map(int, input().split())
prevMoon, moonCyc = map(int, input().split())

years = 0
while prevSun != 0 or prevMoon != 0:
    years += 1
    prevSun = (prevSun+1)%sunCyc
    prevMoon = (prevMoon+1)%moonCyc
print(years)
