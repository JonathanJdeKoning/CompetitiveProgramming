for _ in range(int(input())):
    x,y,k = map(int, input().split())
    ans = []
    tot = 0
    for i in range(1,k):
        ans.append((x,y+i))
        tot += i
    ans.append((x,y-tot))

    for x,y in ans:
        print(x,y)



