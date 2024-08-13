n = input()

if len([c for c in n if c not in "14"]) >0: exit(print("NO"))
if "444" in n:
    exit(print("NO"))

n = n.replace("144","")
while True:
    old = n
    n = n.replace("11", "1")
    if len(n) == len(old):
        break

n = n.replace("14","")

if not n or n == "1":
    print("YES")
else:
    print("NO")
