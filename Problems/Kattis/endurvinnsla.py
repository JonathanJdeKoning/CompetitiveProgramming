city = input()
allowed = float(input())

items = int(input())
plast = 0
for i in range(items):
    bagtype = input()
    if bagtype != "plast":
        plast += 1
    else:
        continue

perc = plast/items

if perc <= allowed:
    print("Jebb")
else:
    print("Neibb")
