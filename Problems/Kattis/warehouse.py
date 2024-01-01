tests = int(input())

for test in range(tests):
    mydict = {}
    items = int(input())

    for _ in range(items):
        name, count = input().split()
        count = int(count)

        if name not in mydict:
            mydict[name] = count
        else:
            mydict[name] += count
    print(len(mydict))
    new = sorted(mydict.items(), key=lambda x: (-x[1],x[0]))

    for thingo in new:
        print(f"{thingo[0]} {thingo[1]}")
