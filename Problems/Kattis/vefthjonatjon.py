lines = int(input())

x, y, z = 0,0,0
for line in range(lines):
    
    a, b, c = input().split()
    
    if a == "J": x+=1
    if b == "J": y += 1
    if c == "J": z+= 1
print(min([x,y,z]))