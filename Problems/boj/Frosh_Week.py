N,M = list(map(int, input().replace(","," ").split()))
tasks = sorted(list(map(int, input().replace(","," ").split())))
times = sorted(list(map(int, input().replace(","," ").split())))
ans = 0
while tasks and times:
    currslot = times.pop()
   
    while True:
        
        currtask = tasks.pop()
        
        if currtask <= currslot:
            ans +=1
            break
        if not tasks: break
print(ans)

