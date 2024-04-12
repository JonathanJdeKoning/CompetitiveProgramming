from fractions import Fraction
y,w = map(int, input().split())

mx = max([y,w])
poss = list(range(1,7))

good = []
for i in range(1,7):
    if i>=mx:
        good.append(i)
f=str(Fraction(len(good),6))
if f == "0":
    print("0")
elif f=="1":
    print("1/1")
else:
    print(f)



