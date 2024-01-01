mylen = int(input())
s = input() +"z"
pos = []
buf = ""
for c in s:
    if c.isdigit():
        buf+= c
    else:
        if buf != "":
            pos.append(int(buf))
            buf = ""
print(max(pos))
