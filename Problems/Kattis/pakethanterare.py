prods, stores = list(map(int, input().split()))

storeprods = list(map(int, input().split()))


latestdict = {}
for i in range(prods):
    prod = input().split()
    latestdict[prod[0]] = int(prod[1])
for store in range(stores):
    total = 0
    for prod in range(storeprods[store]):
        proddo = input().split()
        val = int(proddo[1])

        total += latestdict[proddo[0]] - val
    print(total)
