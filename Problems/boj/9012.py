for _ in range(int(input())):
    s = input()
    stack = 0

    for c in s:
        if c == "(":
            stack += 1
        else:
            stack -= 1
            if stack ==-1:
                print("NO"); break
    else:
        if stack == 0:
            print("YES")
        else:
            print("NO")

