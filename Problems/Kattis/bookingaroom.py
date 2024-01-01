rooms, booked = list(map(int, input().split()))

if rooms == booked:
    print("too late")
else:
    roomlist = list(range(1,rooms+1))
    for booking in range(booked):
        roomnum = int(input())
        roomlist.remove(roomnum)
    print(roomlist[0])