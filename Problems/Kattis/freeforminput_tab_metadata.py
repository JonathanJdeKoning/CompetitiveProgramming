while True:
    try:
        s = input().split(",")
    except: break
    tot = 0

    for num in s:
        tot += float("".join(num.split()))
    print(tot)