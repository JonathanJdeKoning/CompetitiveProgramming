from collections import defaultdict
for _ in range(int(input())):
    d = defaultdict(int)    
    for _ in range(int(input())):
        data = input().split()
        d[data[1]] += 1

    arr = d.values()
    total = 1
    for num in arr:
        total *= num+1

    print(total-1)


