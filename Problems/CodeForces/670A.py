n = int(input())

weeks, days = divmod(n,7)

base = weeks*2
if days == 0:
    print(base, base)
else:
    if days == 6:
        print(base+1, base+2)
    elif days == 1:
        print(base, base+1)
    else:
        print(base, base+2)
