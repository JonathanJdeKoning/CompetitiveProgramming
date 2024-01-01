start = int(input())
qs = int(input())
timeleft = 210

for _ in range(qs):
    q = input().split()
    ans = q[1]
    time = int(q[0])


    if timeleft -time <=0:
        if timeleft-time == 0 and ans == "T":
            start+= 1
            if start == 9:
                start = 1
        print(start)
        break

    if ans == "T":
        start+=1

    if start == 9:
        start = 1
    
    timeleft -= time

