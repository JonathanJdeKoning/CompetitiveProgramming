for i in range(8):
    print(bin(i)[2:].zfill(3), end = "")
    print(f" / {i}", end = "")
    print(" -> ", end="")
    s = i^1

    print(bin(s)[2:].zfill(3), end = "")
    print(f" / {s}")