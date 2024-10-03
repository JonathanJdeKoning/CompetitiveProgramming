ops = ["+", "-", "//", "*"]

a,b,c,d = map(int, input().split())

good = set()

for op1 in ops:
    for op2 in ops:
        eq = f"{a} {op1} {b} == {c} {op2} {d}"
        try:
            if eval(eq):
                good.add(eq.replace("==", "=").replace("//", "/"))
        except: pass
good = sorted(good)
if not good: print("problems ahead")
else:
    for eq in good:
        print(eq)