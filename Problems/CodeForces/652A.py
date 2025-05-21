x, y = list(map(int, input().replace(","," ").split()))
gain, loss = list(map(int, input().replace(","," ").split()))

time = 14 
day = 0 
c = x
while True:
    if time >= 10 and time < 22:
        c += gain
    else:
        c -= loss

    if c >= y:
        exit(print(day))

    time = (time+1)%24
    if time == 10:
        day += 1
    
    
    if time == 14 and c <= x and day > 2:
        exit(print(-1))
