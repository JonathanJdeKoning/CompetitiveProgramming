numlists, numitems = list(map(int, input().split()))

lists = []

ingredients = {

}

for i in range(numlists):
    lists.append(input().split())

for list in lists:
    for item in list:
        if item in ingredients:
            ingredients[item] += 1
        else:
            ingredients[item] = 1

goods = []

for item, count in ingredients.items():
    if count == numlists:
        goods.append(item)
print(len(goods))
print("\n".join(sorted(goods)))