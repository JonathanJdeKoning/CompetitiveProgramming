n = float(input())

if n.is_integer():
    print(f"int {int(n)}")
else:
    nt = int(n//1)
    flt = "0." + str(n).split(".")[1]
    print(f"float {nt} {flt}")
