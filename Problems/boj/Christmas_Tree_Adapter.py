a = int(input())
w,v = list(map(int, input().split()))
if w//v >= a:
    print(1)
else:
    print(0)
