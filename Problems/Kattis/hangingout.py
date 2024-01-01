limit, events = list(map(int, input().split()))

curr = 0
denied = 0
for i in range(events):
    line = input().split()
    command = line[0]
    num = int(line[1])
    
    if command == "enter":
        if num + curr > limit:
            denied += 1
            continue
        else:
            curr += num
    if command == "leave":
        curr -= num
print(denied)
    
    