n = int(input())
a = list(map(int, input().split()))
if sum(a)%len(a)==0:
    print(len(a))
else:
    print(len(a)-1)
