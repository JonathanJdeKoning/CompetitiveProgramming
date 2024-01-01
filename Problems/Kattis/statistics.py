count = 0
while True:
    try:
        count += 1
        mylist = list(map(int, input().split()))[1:]
        maxi = max(mylist)
        mini = min(mylist)
        rnge = maxi-mini
        print(f"Case {count}: {mini} {maxi} {rnge}")
    except EOFError:
        break
