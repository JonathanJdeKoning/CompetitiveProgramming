for _ in range(int(input())):
    N = int(input())
    curr = 0
    need = 8
    x = 1
    while N >= need:
        curr += 1
        x += 2
        N -= need
        need = x*4+4
    print(curr)
