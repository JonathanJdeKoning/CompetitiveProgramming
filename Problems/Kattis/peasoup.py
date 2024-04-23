numstraunts = int(input())
found = False
for _ in range(numstraunts):
    numitems = int(input())
    name = input()
    
    items = []
    for _ in range(numitems):
        items.append(input())
    if "pea soup" in items and "pancakes" in items:
        print(name)
        found = True
        break
if not found:
    print("Anywhere is fine I guess")
    
