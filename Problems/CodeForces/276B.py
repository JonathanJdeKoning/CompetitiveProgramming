a,b,n = map(int, input().split())
for i in range(10):
    if int(str(a)+str(i))%b ==0:
        exit(print(str(a)+str(i)+"0"*(n-1)))
print(-1)

