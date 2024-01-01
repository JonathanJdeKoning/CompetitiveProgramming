a,b,c = list(map(int, input().split()))

def oppo(x,y):
    return((x^y)<0)

if b-a == c-b:
    print("cruised")

if abs(b-a) > abs(c-b):
    if oppo(b-a,c-b):
        print("turned")
    else:
        print("braked")


if abs(b-a) < abs(c-b):
    if oppo(b-a,c-b):
        print("turned")
    else:
        print("accelerated") 
