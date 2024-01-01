cases = int(input())

for case in range(cases):
    guests = int(input())
    
    guestnums = list(map(int, input().split()))
    
    for guestnum in guestnums:
        if guestnums.count(guestnum) == 1:
            print(f"Case #{case+1}: {guestnum}")