for _ in range(int(input())):
    a,b = map(int, input().split())
    print(sum([x for x in list(range(min(a,b)+1,max(a,b))) if x%2!=0]))

