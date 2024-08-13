
for _ in range(int(input())):
    mat = []
    R,C = map(int, input().split())
    x = None
    first = None
    last = None
    done = False
    for i in range(R):
        row = input()
        if done: continue
        if first is None or x is None:
            c = row.count("#")
            if c:
                first = i
                last = i
                x = row.index("#")
                if i==R-1:
                    print(i+1, x+1)
        else:
            if row[x] != "#" or i==R-1:
                last = i
                print(1+(first+last)//2, x+1)
                done = True

