while True:
    try:
        a,b = map(int, input().split())
        a += 1

        print(b//a)
    except: break
