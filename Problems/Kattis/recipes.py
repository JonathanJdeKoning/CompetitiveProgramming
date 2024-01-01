numcases = int(input())

for i in range(numcases):
    print(f"Recipe # {i+1}")
    ings = {}
    magic = 0
    numingredients, numportions, desiredportions = list(map(int, input().split()))
    scale = desiredportions/numportions
    for i in range(numingredients):
        data = input().split()
        if data[2] == "100.0":
            magic = float(data[1])*float(scale)
        ings[data[0]] = {"weight": float(data[1]), "perc": float(data[2])}

    for key, val in ings.items():
        print(f"{key} {(magic*val['perc'])/100}")
    print("-"*40)
