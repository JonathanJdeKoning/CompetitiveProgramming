for _ in range(int(input())):
    n = int(input())
    s = input()
    unan = 0
    for c in s:
        if c == "Q":
            unan += 1 
        elif c == "A":
            unan = max(0,unan-1)

    if unan != 0:
        print("No")
    else:
        print("Yes")
