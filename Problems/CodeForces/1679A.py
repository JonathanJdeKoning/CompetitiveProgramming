for _ in range(int(input())):
    N = int(input())
    mn = None
    mx = None
    if N%2==1 or N < 4: 
        print(-1)
        continue
    if N==4:
        print(1,1)
        continue

    mx = N//4
    if N%6 == 0:
        mn = N//6
    elif N%6==2:
        mn = (2+((N//6)-1))
    elif N%6 ==4:
        mn = (1 + (N-4)//6)

    
    print(mn,mx)
