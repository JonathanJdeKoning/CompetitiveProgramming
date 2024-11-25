for _ in range(int(input())):
    input()
    N = int(input())
    candy = [int(input()) for _ in range(N)]
    t = sum(candy)
    if t%N==0: print("YES")
    else: print("NO")