for _ in range(int(input())):
    a = input().split(",")
    tot = 0

    for i in range(len(a)):
        num = a[~i]
        if not num:
            num = 0
        else:
            num = int(num)
        tot += num*(60**(i))
    print(tot)
