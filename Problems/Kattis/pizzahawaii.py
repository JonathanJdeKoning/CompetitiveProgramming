tc = int(input())
for _ in range(tc):
    pizzas = int(input())
    seen = {}
    ingredients = {}
    first = True
    for i in range(pizzas):
        pizza = input()
        italy = input().split()[1:]
        english = input().split()[1:]
        

        for ing in italy:
            if ing not in ingredients:
                ingredients[ing] = list(filter(lambda x:x not in seen,english[:]))
            else:
                for eng in ingredients[ing].copy():
                    if eng not in english:
                        ingredients[ing].remove(eng)
                        print("REMOVED")
        for key, value in ingredients.items():
            if key not in italy:
                for ing in english[:]:
                    try:
                        ingredients[key].remove(ing)
                    except:
                        pass
        seen = set(list(seen)+ english)

    accounted = []
    for key, item in ingredients.items():
        if len(item) == 1:
            accounted.append(item[0])
    for key, item in ingredients.items():
        if len(item) >1:
            for ing in item[:]:
                if ing in accounted:
                    ingredients[key].remove(ing) 
    ingredients = dict(sorted(ingredients.items()))
    for item, val in ingredients.items():
        x = sorted(val)
        for y in x:
            print(f"({item}, {y})")
    print()


