a,b,c,d = map(int, input().split())

vash = max((3*b)/10, b- ((b/250) * d))
mish = max((3*a)/10, a- ((a/250) * c))

if vash > mish:
    print("Vasya")
elif mish > vash:
    print("Misha")
else:
    print("Tie")
