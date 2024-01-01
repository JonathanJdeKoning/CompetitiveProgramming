y, p = input().split()

if y.endswith("e"):
    print(y+"x"+p)
elif y[-1] in "aiou":
    print(y[:-1]+"ex"+p)
elif y.endswith("ex"):
    print(y+p)
else:
    print(y+"ex" + p)