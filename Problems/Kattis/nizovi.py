spaces = 0
s = input()
arr = []
run = []
for c in s:
    if c not in "abcdefghijklmnopqrstuvwxyz":
        arr.append("".join(run))
        run = []
        arr.append(c)
    else:
        run.append(c)
arr.append(run)
arr = [x for x in arr if x]
arr.append("#")
back = 0
for i,token in enumerate(arr[:-1]):
    if token == "}":
        spaces -= 2
    if token ==",":
        back = spaces
        spaces = 0
    print(" "*spaces, end="")
    
    if token == "}":
        if arr[i+1] == ",":
            print("}",end="")
        else:
            print("}")
    elif token == "{":
        spaces += 2
        if arr[i+1] == ",":
            print("{", end="")
        else:
            print("{")
    elif token == ",":
        print(",")
        spaces = back
    else:
        if arr[i+1] == ",":
            print(token, end="")
        else:
            print(token)
    

