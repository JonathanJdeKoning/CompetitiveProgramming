x,y,z = list(map(int, input().split()))
ops = "+-*/"

goodop= None
top = True
for op in ops:
    try:
        res = eval(f"{x}=={y}{op}{z}")
        if res:
            goodop = op
            top = True
            break
        res = eval(f"{x}{op}{y}=={z}")
        if res:
            goodop = op
            top = False
            break
    except ZeroDivisionError:
        continue

if top:
    print(f"{x}={y}{goodop}{z}")
else:
    print(f"{x}{goodop}{y}={z}")
