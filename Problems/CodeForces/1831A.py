for tc in range(int(input())):
    N = int(input()) 
    A = list(map(int, input().replace(","," ").split()))
    B = []
    for num in A:
        B.append(1+ (N- num))
    print(" ".join(map(str, B )))
     
    
    