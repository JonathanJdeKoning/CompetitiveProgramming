mycount = 1
while True:
    try:
        e, m = list(map(int, input().split()))

        count = 0

        e = int(e)
        m = int(m)

        while (True):
            
            if e == 0:
                if m == 0:
                    break
            e+=1
            m+=1
            
            if e==365:
                e = 0
            if m == 687:
                m = 0
            count += 1
        
        print(f"Case {mycount}: {count}")
        mycount += 1
    except EOFError:
        break        