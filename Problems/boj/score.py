for _ in range(int(input())):
    s = input()
    total = 0
    curr = 0
    for c in s:
        if c == "O":
            curr += 1
        else:
            curr = 0
        total += curr
    print(total)

