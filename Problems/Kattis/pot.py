import math
numnums = int(input())
total = 0

for _ in range(numnums):
    num = input()
    
    power = num[-1]
    
    base = num[:-1]
    total += math.pow(int(base), int(power))

print(int(total))
    
    
    
    
    