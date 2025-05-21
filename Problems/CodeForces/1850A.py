for tc in range(int(input())):
    A = list(map(int, input().replace(","," ").split()))
    A.sort()
    
    if A[-1] + A[-2] >= 10:
        print("YES")
    else:
        print("NO")
    
    