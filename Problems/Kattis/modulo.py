dist = []
for i in range(10):
    num = int(input())
    
    if num%42 not in dist:
        dist.append(num%42)
print(len(dist))