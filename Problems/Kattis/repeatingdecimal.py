while True:
    try:
        a,b,c = map(int, input().split())
    except: break
    from decimal import Decimal, getcontext

    getcontext().prec = c+3

    s = str(Decimal(a)/Decimal(b))
    if "." not in s:
        s = s + "." + "0"
    pad = s+ "0"*c
    print(pad[:s.index(".") +c+1])

