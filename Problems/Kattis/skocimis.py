a,b,c = list(map(int, input().split()))

huh = ""
for i in range(c+1):
    if i == a or i ==b or i ==c:
        huh+="#"
    else:
        huh += "-"

huh = huh.strip("-")
print(max([len(x) for x in huh.split("#")]))
