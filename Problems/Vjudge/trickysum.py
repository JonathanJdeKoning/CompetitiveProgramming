for _ in range(int(input())):
    n = int(input())
    total = (n*(n+1))//2
    
    exp = 0
    while True:
        x = 2**exp
        if x > n:
            break
        else:
            total-=2*x
            exp += 1
    print(total)

