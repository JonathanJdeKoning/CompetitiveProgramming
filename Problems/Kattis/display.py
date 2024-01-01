nums = {
    "0":"+||+||+\n-     -\n-     -\n-     -\n+||+||+\n       \n       ",
    "1":"       \n       \n       \n       \n+||+||+\n       \n       ",
    "2":"+||+  +\n-  -  -\n-  -  -\n-  -  -\n+  +||+\n       \n       ",
    "3":"+  +  +\n-  -  -\n-  -  -\n-  -  -\n+||+||+\n       \n       ",
    "4":"   +||+\n   -   \n   -   \n   -   \n+||+||+\n       \n       ",
    "5":"+  +||+\n-  -  -\n-  -  -\n-  -  -\n+||+  +\n       \n       ",
    "6":"+||+||+\n-  -  -\n-  -  -\n-  -  -\n+||+  +\n       \n       ",
    "7":"      +\n      -\n      -\n      -\n+||+||+\n       \n       ",
    "8":"+||+||+\n-  -  -\n-  -  -\n-  -  -\n+||+||+\n       \n       ",
    "9":"+  +||+\n-  -  -\n-  -  -\n-  -  -\n+||+||+\n       \n       ",
    ":":"  o o  \n       \n       "
}


while True:
    data = input()
    if data == "end":
        break
    out = []
    for c in data:
        num = nums[c].split("\n")
        for line in num:
            out.append(line)
    out = out[:-2]
    
    for i in range(6,-1,-1):
        new = ""
        for c in out:
            new += c[i]
        print(new)
    print()
    print()
print("end")
