slen = int(input())
s = input()

stack = []
bad = False
for i,c in enumerate(s):
    if c in "{([":
        stack.append(c)
    elif c in "}])":
        try:
            last = stack[-1]
        except: 
            print(c,i)
            bad = True
            break
        if c == ")" and stack[-1]!= "(":
            print(c,i)
            bad = True
            break
        if c == "]" and stack[-1]!= "[":
            print(c,i)
            bad = True
            break
        if c == "}" and stack[-1]!= "{":
            bad = True
            print(c,i)
            break
        stack.pop(-1)
if not bad:
    print("ok so far")



