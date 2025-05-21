while True:
    try:
        start, end = input().split()
    except EOFError: break
    sh, sm, ss = map(int, start.split(":"))
    eh, em, es = map(int, end.split(":"))

    ans = 0

    while True:
        num = int(str(sh) + str(sm).zfill(2) + str(ss).zfill(2))
        if num%3 == 0:
            ans += 1
            #print(f"   {num}")
        if sh == eh and sm == em and ss == es:
            print(ans)
            break

        ss += 1
        if ss == 60:
            ss = 0
            sm += 1
            if sm == 60:
                sm = 0
                sh += 1
                if sh == 24:
                    sh = 0
        