base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    myin = input().split()

    rot = int(myin[0])
    if rot == 0: break
    string = myin[1][::-1]

    new = ""
    for c in string:
        whereis = base.index(c)

        newindex = (whereis+rot)%28

        new+=base[newindex]
    print(new)
    
    
    


