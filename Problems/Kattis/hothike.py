days = int(input())

daylist = list(map(int, input().split()))


mini = 100
for i in range(len(daylist)-2):
    if max([daylist[i],daylist[i+2]]) < mini:
        mini = max([daylist[i], daylist[i+2]])

for i in range(len(daylist)-2):
    if max([daylist[i],daylist[i+2]]) == mini:
        print(f"{i+1} {max([daylist[i],daylist[i+2]])}")
        break



