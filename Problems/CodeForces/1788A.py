for tc in range(int(input())):
    N = int(input())
    A = list(map(int, input().replace(","," ").split()))
    twos = A.count(2)
    if twos%2 == 1: 
        print(-1)
        continue
    
    seek = twos//2
    curr = 0
    for i,c in enumerate(A, start=1):
        if c == 2:
            curr += 1
           
        
        if curr == seek:
            print(i)
            break
        
        