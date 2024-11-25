for _ in range(int(input())):
    p1 = 0
    p2 = 0
    for _ in range(int(input())):
        n, m = input().split()
        if n == m: continue

        if n == "R":
            if m == "S":
                p1 += 1
            else:
                p2 += 1
        elif n == "P":
            if m == "R":
                p1 += 1
            else:
                p2 += 1
        elif n == "S":
            if m == "P":
                p1 += 1
            else:
                p2 += 1
        else:
            5/0
    if p1 > p2:
        print("Player 1")
    elif p2 > p1:
        print("Player 2")
    else:
        print("TIE")