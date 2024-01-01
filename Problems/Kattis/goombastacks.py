rooms = int(input())

totalgoombs = 0
output = ""
for room in range(rooms):
    goombs, needed = list(map(int, input().split()))
    
    totalgoombs += goombs
    
    if totalgoombs < needed:
        output += "im"
        break
output += "possible"
print(output)
        