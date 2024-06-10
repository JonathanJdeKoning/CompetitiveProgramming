n = int(input())
if n%400 == 0:
    print(1)
elif n%4==0:
    if n%100==0:
        print(0)
    else:
        print(1)
else:
    print(0)
