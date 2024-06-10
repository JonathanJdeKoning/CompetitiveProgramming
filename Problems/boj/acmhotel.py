for _ in range(int(input())):
    floors, rooms, idx = map(int, input().split())

    curr = 1
    found = False
    for room in range(1,rooms+1):
        for floor in range(1, floors+1):
            if curr == idx:
                print(f"{floor}{str(room).zfill(2)}")
                found = True
                break;
            curr += 1
        if found: break

