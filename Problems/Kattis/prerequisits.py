while True:
    data = input().split()
    if data[0] == "0": break

    cats = int(data[1])
    chosen = list(map(int, input().split()))
    
    good = True
    for _ in range(cats):
        
        data = list(map(int, input().split()))
        req = data[1]
        courses = data[2:]

        for course in chosen:
            if course in courses:
                req -= 1
        if not req <= 0:
            good = False
    if good:
        print("yes")
    else:
        print("no")


