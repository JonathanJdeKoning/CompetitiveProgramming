t1,e1,f1 = list(map(int, input().split()))
t2,e2,f2 = list(map(int, input().split()))

mx = 3*t1 + 20*e1 + 120*f1
ml = 3*t2 + 20*e2 + 120*f2

if mx > ml:
    print("Max")
elif ml > mx:
    print("Mel")
else:
    print("Draw")