cost = float(input())
lawns = int(input())
total = 0
for lawn in range(lawns):
    width, length = list(map(float, input().split()))
    
    total += (width*length)*cost
print(total)
    