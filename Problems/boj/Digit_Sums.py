while True:
    N= int(input())
    if N == 0: break

    while N >= 10:
        N = sum([int(x) for x in str(N)])
    print(N)