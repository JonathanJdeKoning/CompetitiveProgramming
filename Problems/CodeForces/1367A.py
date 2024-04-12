for _ in range(int(input())):
    s = input()
    if len(s) == 2:
        print(s)
        continue
    for i in range(0,len(s),2):
        print(s[i],end="")
    print(s[-1])

