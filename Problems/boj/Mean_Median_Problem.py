while True:
    A, B = list(map(int, input().replace(","," ").split()))
    if A ==0 and B==0: break
    print(A - (B-A))