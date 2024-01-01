trans = int(input())

mini = 0
total = 0
for i in range(trans):
    num = int(input())
    total += num
    if total< mini:
        mini = total
print(abs(mini))
    
