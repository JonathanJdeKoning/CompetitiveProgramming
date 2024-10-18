while True:
    check = [0]*10
    #print(check)
    ans = "Stan may be honest"
    done = False
    while True:
        n = int(input())
        n -= 1
        if n == -1:
            done = True
            break
        d = input()
        if d == "too high":
            if -1 in check[n:]:
                ans = "Stan is dishonest"
            check[n] = 1
        elif d == "too low":
            if 1 in check[:n+1]:
                ans = "Stan is dishonest"
            check[n] = -1
        elif d == "right on":
            if 1 in check[:n+1] or -1 in check[n:]:
                ans = "Stan is dishonest"
            print(ans)
            break
    if done: break
