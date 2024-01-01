cars = int(input())
distance = float(input())

maxi = 0
winner = ""
for car in range(cars):
    id, vel, fuel = list(input().split())
    vel = float(vel)
    fuel = float(fuel)
    
    rof = fuel/(distance/vel)
    efficiency = vel/rof
    if efficiency > maxi:
        maxi = efficiency
        winner = id
print(winner)
