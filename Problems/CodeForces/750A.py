n,k = map(int, input().split())
found = False
timeleft = 240
if k > 235:
    print("0")
    found = True
else:
    total = 0
    for i in range(1,n+1):
        timeleft -= i*5
        total += 1
        if timeleft < k:
            print(total-1)
            found = True
            break
if not found:
    print(n)

    

