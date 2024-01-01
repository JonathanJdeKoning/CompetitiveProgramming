g, s, c = list(map(int, input().split()))

bp = g*3+s*2+c*1

vic = ""
tres= ""

if bp >= 8: vic = "Province"
elif bp >= 5: vic = "Duchy"
elif bp >= 2: vic = "Estate"

if bp >= 6: tres = "Gold"
elif bp >= 3: tres = "Silver"
else: tres = "Copper"

if vic == "":
    print("Copper")
else:
    print(f"{vic} or {tres}")
