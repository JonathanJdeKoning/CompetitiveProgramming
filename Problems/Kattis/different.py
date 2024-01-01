while True:
    try:
        n,m = list(map(int, input().split()))
        print(abs(n-m))
        
    except EOFError:
        break