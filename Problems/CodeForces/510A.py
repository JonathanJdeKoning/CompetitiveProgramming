n,m = map(int, input().split())

out = []

for i in range(1,n+1):
    if i%2 ==1:
        out.append(["#"]*m)
    else:
        if i%4!=0:
            row = ["."]*(m-1)
            row.append("#")
            out.append(row)
        else:
            row = ["#"]
            row.extend(["."]*(m-1))
            out.append(row)
for row in out:
    print("".join(row))
