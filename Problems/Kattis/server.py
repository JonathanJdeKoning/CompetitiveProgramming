numtasks, time = list(map(int, input().split()))
tasks = list(map(int, input().split()))
count = 0
for task in tasks:
    count += 1 if time-task >= 0 else 0  
    time -= task
print(count)
    