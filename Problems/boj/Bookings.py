while True:
    s, curr = input().split()
    if s == "#": break
    curr = int(curr)

    while True:
        op, num = input().split()
        if op == "X":
            print(s, curr); break
        num = int(num)

        if op == "B":
            if curr + num >68: continue
            curr += num
        elif op == "C":
            if curr - num < 0: continue
            curr -= num

