n = int(input())

mat = []
mat.append("  " + "H "*n)
mat.append("  " + "| "*n)
mat.append("H-" + "C-"*n + "OH")
mat.append("  " + "| "*n)
mat.append("  " + "H "*n)

for r in mat:
    print(r)