for _ in range(int(input())):
    mat = []
    for _ in range(8):
        mat.append(list(input()))

    for i in range(8):
        col = [row[i] for row in mat]
        if len([x for x in col if x =="."]) != 8:
            print("".join(col).replace(".",""))
