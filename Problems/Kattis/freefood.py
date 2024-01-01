dayses = int(input())

days = []
for i in range(dayses):
    start, stop = list(map(int, input().split()))
    
    for i in range(start, stop+1):
        if i not in days:
            days.append(i)

print(len(days))