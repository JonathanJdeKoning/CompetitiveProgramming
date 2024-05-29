
x,y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

bPtr = 0
for num in a:
    if num == b[bPtr]:
        bPtr += 1
        if bPtr == len(b):
            print("YES")
            break
else:
    print("NO")
