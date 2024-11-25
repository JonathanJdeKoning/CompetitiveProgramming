for i in range(1,10000000):
    digs = sorted(list(str(i)))

    for j in range(2,7):
        if sorted(list(str(i*j))) != digs:
            break
    else:
        print(i)
        break