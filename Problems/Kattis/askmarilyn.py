
rude = 0
notrude = 0
for _ in range(1000):
    print("A")

    shown, val = input().split()
    if val == "1":
        print(shown)
        input()
        continue


    elif val == "0":
        if shown == "B":
            choice = "C" if notrude > rude else "A"
            print(choice)
            res, door = input().split()
            if door == "C":
                notrude +=1
            else:
                rude += 1
            continue
        else:
            choice = "B" if notrude> rude else "A"
            print(choice)
            res, door = input().split()
            if door == "B":
                notrude +=1
            else:
                rude += 1
            continue
