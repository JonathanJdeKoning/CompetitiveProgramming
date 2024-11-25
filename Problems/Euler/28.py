curr = 1
ans = 1

jump = 2
while True:
    for i in range(4):
        curr += jump
        ans += curr
        if curr == 1002001:
            exit(print(ans))
            
    jump += 2