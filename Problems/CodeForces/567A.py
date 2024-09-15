n = int(input())
a = list(map(int, input().split()))
for i, x in enumerate(a):
    if i==0: print(a[1]-x, a[-1]-x)
    elif i == len(a)-1: print(x-a[-2], x-a[0])

    else:
        print(min(a[i+1]-x, x-a[i-1]), max(a[-1]-x, x-a[0]))

