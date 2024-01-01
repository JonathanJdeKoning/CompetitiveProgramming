a,b,c,d = list(map(int, input().split()))

print(len([x for x in list(range(a,b+1)) if x%(c)==0 and x%(d)==0]))
