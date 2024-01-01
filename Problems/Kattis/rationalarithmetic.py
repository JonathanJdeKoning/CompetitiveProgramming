from fractions import Fraction
tests = int(input())

for i in range(tests):
    data = input().split()
    x1 = int(data[0])
    y1 = int(data[1])
    op = data[2]
    x2 = int(data[3])
    y2 = int(data[4])
    
    out1 = Fraction(x1, y1)
    out2 = Fraction(x2,y2)

    if op == "+":
        output = str(out1+out2).split("/")
        try:
            print(f"{output[0]} / {output[1]}")
        except:
            print(f"{output[0]} / 1")
    elif op == "-":
        output = str(out1-out2).split("/")
        try:
            print(f"{output[0]} / {output[1]}")
        except:
            print(f"{output[0]} / 1")
    elif op == "*":
        output = str(out1*out2).split("/")
        try:
            print(f"{output[0]} / {output[1]}")
        except:
            print(f"{output[0]} / 1")
    elif op == "/":
        output = str(out1/out2).split("/")
        try:
            print(f"{output[0]} / {output[1]}")
        except:
            print(f"{output[0]} / 1")
