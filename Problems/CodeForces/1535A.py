for tc in range(int(input())):
    a,b,c,d = list(map(int, input().replace(","," ").split()))
    A = sorted([a,b,c,d])
    C = [a,b,c,d]
    win = sorted([A[-1], A[-2]])
    B = sorted([max(C[0], C[1]), max(C[2], C[3])])
    
    
    if B == win:
        print("YES")
    else:
        print("NO")
    