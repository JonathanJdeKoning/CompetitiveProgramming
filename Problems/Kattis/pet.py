maxpoints = 0
maxnum = 0

for i in range(1,6):
    
    points = sum(list(map(int, input().split())))
    
    if points > maxpoints:
        maxpoints = points
        maxnum = i
print(f"{maxnum} {maxpoints}")
    