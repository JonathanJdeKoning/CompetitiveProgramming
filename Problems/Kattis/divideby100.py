n = input()
m = input()
n = n.zfill(len(m))
if m == "1":
    exit(print(n))
place = m.count("0")
new = (n[:-place] + "." + n[-place:]).rstrip("0")

if new[:new.index(".")] == "0"*new.index("."):
    new = "0."+new[new.index(".")+1:]
else:
    new = new.lstrip("0")
if new[-1] == ".":
    new = new[:-1]
print(new)
    
